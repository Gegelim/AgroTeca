import sqlite3


def conectar_banco():
    return sqlite3.connect("database.db")


def criar_banco():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conteudos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            categoria TEXT NOT NULL,
            tipo TEXT,
            autor TEXT,
            arquivo TEXT,
            status TEXT DEFAULT 'pendente'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT NOT NULL,
            unidade TEXT NOT NULL,
            preco_atual REAL NOT NULL,
            preco_anterior REAL,
            fonte TEXT,
            data_atualizacao TEXT,
            tendencia TEXT
        )
    """)

    conexao.commit()
    conexao.close()
