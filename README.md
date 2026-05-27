# 🚚 Delivery API FastAPI

Uma API REST moderna para gerenciamento de delivery desenvolvida com Python e FastAPI.

---

# ✨ Funcionalidades

- 📦 Gerenciamento de pedidos
- 👤 Cadastro de usuários
- ⚡ API rápida e performática
- 📄 Documentação automática com Swagger
- ✅ Validação de dados com Pydantic
- 🗄️ Integração com banco de dados
- 🔥 Estrutura simples e organizada

---

# 🛠️ Tecnologias Utilizadas

<div align="left">

<img src="https://skillicons.dev/icons?i=python,fastapi,sqlite" />

</div>

- Python
- FastAPI
- SQLite
- Uvicorn
- Pydantic

---

# 📂 Estrutura do Projeto

```bash
DELIVERY-API-FASTAPI/
│
├── main.py
├── requirements.txt
├── README.md
└── .env
```

Projeto mantido com uma estrutura simples e direta, focada em aprendizado e desenvolvimento backend.

---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/Prabovn7/delivery-api-fastapi.git
```

---

## 2️⃣ Entre na pasta do projeto

```bash
cd delivery-api-fastapi
```

---

## 3️⃣ Crie um ambiente virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / MacOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 4️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Execute o servidor

```bash
uvicorn main:app --reload
```

Servidor rodando em:

```bash
http://127.0.0.1:8000
```

---

# 📚 Documentação da API

## Swagger UI

```bash
http://127.0.0.1:8000/docs
```

## ReDoc

```bash
http://127.0.0.1:8000/redoc
```

---

# 📌 Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | / | Rota principal |
| GET | /docs | Swagger UI |
| GET | /redoc | ReDoc |

---

# 🚀 Melhorias Futuras

- [ ] Autenticação JWT
- [ ] PostgreSQL
- [ ] Docker
- [ ] Testes automatizados
- [ ] Deploy na nuvem
- [ ] CI/CD com GitHub Actions

---

# 🧠 Aprendizados

Este projeto foi desenvolvido para praticar:

- Desenvolvimento Backend
- APIs REST
- FastAPI
- Estruturação de projetos Python
- Validação de dados
- Integração com banco de dados

---

# 👨‍💻 Autor

## Pablo Vinicius

- GitHub: https://github.com/Prabovn7

---

# ⭐ Apoie o Projeto

Se gostou do projeto, deixe uma estrela no repositório.

---

# 📜 Licença

Este projeto está sob a licença MIT.