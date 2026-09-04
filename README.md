# Delivery API

REST API for order management and user authentication built with **FastAPI**.

The project focuses on backend development concepts such as authentication, authorization, database integration and REST API design.

---

## Features

- JWT authentication
- Access and refresh tokens
- Password hashing with bcrypt
- OAuth2 authentication support
- User authentication and authorization
- Admin permission validation
- Order creation and management
- Add and remove order items
- Order cancellation and completion
- Protected routes
- Automatic API documentation

---

## Technologies

<div align="left">

<img src="https://skillicons.dev/icons?i=python,fastapi,sqlite" height="45" />

</div>

<br>

`Python` · `FastAPI` · `SQLAlchemy` · `SQLite` · `JWT` · `Alembic` · `Pydantic`

---

## Project Structure

```text
delivery-api-fastapi/
│
├── alembic/
│
├── auth_routes.py
├── dependencies.py
├── main.py
├── models.py
├── order_routes.py
├── schemas.py
│
├── alembic.ini
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/Prabovn7/delivery-api-fastapi.git
cd delivery-api-fastapi
```

### Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Use a strong and private value for `SECRET_KEY`.

Never commit your real `.env` file.

---

## Running the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically provides interactive documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## Authentication

The API uses **JWT authentication**.

After a successful login, the API returns:

```json
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "Bearer"
}
```

The access token is used to access protected routes.

The refresh token can be used to generate a new access token.

---

## Main Routes

### Authentication

```text
/auth/
/auth/criar_conta
/auth/login
/auth/login-form
/auth/refresh
```

### Orders

```text
/pedidos/
/pedidos/pedido
/pedidos/pedido/{id_pedido}
/pedidos/pedido/cancelar/{id_pedido}
/pedidos/pedido/finalizar/{id_pedido}
/pedidos/pedido/adicionar-item/{id_pedido}
/pedidos/pedido/remover-item/{id_item_pedido}
/pedidos/listar
/pedidos/listar/pedidos-usuario
```

Order routes require authentication.

Some operations also require administrator privileges or ownership of the order.

---

## Database

The project currently uses **SQLite** with **SQLAlchemy ORM**.

Database migrations are managed with **Alembic**.

---

## Roadmap

- [ ] Automated tests with Pytest
- [ ] PostgreSQL
- [ ] Docker
- [ ] Improved project architecture
- [ ] CI/CD with GitHub Actions
- [ ] Cloud deployment

---

## License

This project is licensed under the **MIT License**.

---

<div align="center">

Developed by [Pablo Vinicius](https://github.com/Prabovn7)

</div>
