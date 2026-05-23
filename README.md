# 🌱 AgroTeca — Biblioteca Comunitária de Jutaiteua

A AgroTeca é uma plataforma digital comunitária criada para preservar, organizar e compartilhar conhecimentos agrícolas, culturais e educativos da comunidade de Jutaiteua, no interior do Pará.

O projeto busca conectar tecnologia e saberes tradicionais amazônicos, permitindo que moradores compartilhem conteúdos que passam por um processo de curadoria antes da publicação.

---

# 🌎 Objetivo do Projeto

Fortalecer a agricultura familiar e valorizar os conhecimentos tradicionais da comunidade através de uma biblioteca digital acessível, colaborativa e sustentável.

---

# 🚀 Funcionalidades Implementadas

## 📚 Biblioteca Comunitária
- Página inicial institucional
- Informações sobre a comunidade
- Técnicas de plantio
- Cartilhas digitais
- Vídeos comunitários
- Página de conteúdos aprovados

---

## 🛡️ Sistema de Curadoria
- Envio de conteúdos pela comunidade
- Aprovação de conteúdos
- Rejeição de conteúdos
- Exclusão de conteúdos
- Edição de conteúdos enviados
- Área administrativa protegida por login

---

## 📂 Upload de Arquivos
- Upload real de PDFs
- Upload de imagens
- Upload de arquivos diversos
- Armazenamento em servidor local
- Visualização de arquivos pelo curador
- Download/abertura pública de cartilhas aprovadas

---

# 🧠 Tecnologias Utilizadas

- Python
- Flask
- SQLite
- HTML5
- CSS3
- Jinja2
- Git
- GitHub

---

# 📂 Estrutura do Projeto

```bash
AGROTECA/
│
├── app.py
├── db.py
├── database.db
├── .gitignore
├── README.md
│
├── static/
│   ├── style.css
│   └── uploads/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── comunidade.html
│   ├── tecnicas.html
│   ├── cartilhas.html
│   ├── videos.html
│   ├── enviar.html
│   ├── conteudos.html
│   ├── admin.html
│   ├── editar_conteudo.html
│   └── login.html
│
└── __pycache__/
```

---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
git clone LINK_DO_REPOSITORIO
```

---

## 2️⃣ Entre na pasta do projeto

```bash
cd AGROTECA
```

---

## 3️⃣ Instale as dependências

```bash
pip install flask
```

---

## 4️⃣ Execute o projeto

```bash
python app.py
```

---

## 5️⃣ Acesse no navegador

```txt
http://127.0.0.1:5000
```

---

# 🔐 Login Administrativo

```txt
Usuário: curador
Senha: 1234
```

---

# 🧩 Funcionalidades Técnicas

## CRUD de Conteúdos

### Create
Enviar conteúdo pela plataforma

### Read
Visualizar conteúdos aprovados

### Update
Editar conteúdos enviados

### Delete
Excluir conteúdos

---

# 🎨 Interface

A interface foi desenvolvida com foco em:
- simplicidade;
- acessibilidade;
- identidade amazônica;
- experiência comunitária;
- navegação intuitiva.

---

# 🌱 Impacto Social

A AgroTeca busca:
- preservar conhecimentos tradicionais;
- incentivar agricultura familiar;
- democratizar acesso à informação;
- fortalecer comunidades rurais;
- integrar tecnologia e cultura amazônica.

---

# 🚧 Próximas Implementações

- Sistema real de usuários
- Busca de conteúdos
- Filtros por categoria
- Upload de vídeos
- Upload de áudios
- Comentários da comunidade
- Dashboard administrativo
- Responsividade mobile avançada
- Deploy online
- Integração com APIs externas
- Inteligência Artificial para apoio à curadoria

---

# 👨‍💻 Desenvolvimento

Projeto acadêmico desenvolvido para o Amazon Hacking, com foco em tecnologia social, sustentabilidade e valorização cultural amazônica.
