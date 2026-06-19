import os
import sqlite3
from contextlib import contextmanager

from werkzeug.security import generate_password_hash

DB_PATH = os.environ.get("AGROTECA_DB_PATH", "database.db")

@contextmanager
def get_db():
    """Context-managed sqlite connection. Commits on success, rolls back on
    exception, and always closes the handle."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def criar_banco():
    with get_db() as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS conteudos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                categoria TEXT NOT NULL,
                tipo TEXT,
                autor TEXT,
                arquivo TEXT,
                status TEXT NOT NULL DEFAULT 'pendente',
                criado_em TEXT
            )
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_conteudos_status ON conteudos(status)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_conteudos_status_categoria ON conteudos(status, categoria)")

        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id               INTEGER PRIMARY KEY AUTOINCREMENT,
                nome             TEXT NOT NULL,
                usuario          TEXT NOT NULL UNIQUE,
                senha            TEXT NOT NULL,
                role             TEXT NOT NULL DEFAULT 'aluno',
                reset_solicitado INTEGER NOT NULL DEFAULT 0
            )
        """)

        _migrar_colunas(cur)
        _seed_admin_if_configured(cur)


def _migrar_colunas(cur):
    """Add columns introduced after the initial schema to databases created by
    an earlier version. CREATE TABLE IF NOT EXISTS never alters an existing
    table, so new columns need an explicit, idempotent migration."""
    user_cols = {row[1] for row in cur.execute("PRAGMA table_info(usuarios)").fetchall()}
    if "reset_solicitado" not in user_cols:
        cur.execute(
            "ALTER TABLE usuarios ADD COLUMN reset_solicitado INTEGER NOT NULL DEFAULT 0"
        )

    cont_cols = {row[1] for row in cur.execute("PRAGMA table_info(conteudos)").fetchall()}
    if "criado_em" not in cont_cols:
        cur.execute("ALTER TABLE conteudos ADD COLUMN criado_em TEXT")


def _seed_admin_if_configured(cur):
    """Seed an initial admin. Uses env vars when set; otherwise falls back to
    fixed defaults so a fresh clone can log in without configuration."""
    admin_user = os.environ.get("AGROTECA_ADMIN_USER", "curador")
    admin_pass = os.environ.get("AGROTECA_ADMIN_PASSWORD", "1234")
    admin_name = os.environ.get("AGROTECA_ADMIN_NAME", "Curador")

    cur.execute("SELECT 1 FROM usuarios WHERE role = 'admin' LIMIT 1")
    if cur.fetchone():
        return

    cur.execute(
        "INSERT INTO usuarios (nome, usuario, senha, role) VALUES (?, ?, ?, 'admin')",
        (admin_name, admin_user, generate_password_hash(admin_pass)),
    )


def buscar_usuario(usuario):
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM usuarios WHERE usuario = ?", (usuario,)
        ).fetchone()
        return dict(row) if row else None


def listar_usuarios():
    """All accounts, with pending password-reset requests surfaced first so a
    curator sees who needs help at the top of the list."""
    with get_db() as conn:
        rows = conn.execute(
            """SELECT id, nome, usuario, role, reset_solicitado
                 FROM usuarios
                ORDER BY reset_solicitado DESC, nome COLLATE NOCASE"""
        ).fetchall()
        return [dict(r) for r in rows]


def contar_resets_pendentes():
    with get_db() as conn:
        return conn.execute(
            "SELECT COUNT(*) FROM usuarios WHERE reset_solicitado = 1"
        ).fetchone()[0]


def marcar_reset_solicitado(usuario_id):
    with get_db() as conn:
        conn.execute(
            "UPDATE usuarios SET reset_solicitado = 1 WHERE id = ?", (usuario_id,)
        )


def redefinir_senha(usuario_id, senha_hash):
    """Set a new password hash and clear any pending reset request."""
    with get_db() as conn:
        conn.execute(
            "UPDATE usuarios SET senha = ?, reset_solicitado = 0 WHERE id = ?",
            (senha_hash, usuario_id),
        )
