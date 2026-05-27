# Delivery FastAPI (Pedidos + Autenticação JWT)

API REST construída com **FastAPI**, **SQLAlchemy (SQLite)** e **JWT**.

## Stack
- FastAPI
- Pydantic (schemas)
- SQLAlchemy
- JWT (python-jose)
- Alembic (migrations)

## Pré-requisitos
- Python 3.10+
- Git (para subir no GitHub)

## Instalação
1. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração (variáveis de ambiente)
Crie um arquivo `.env` na raiz do projeto.

Use o `.env.example` fornecido.

Exemplo:
- `SECRET_KEY`
- `ALGORITHM`
- `ACCESS_TOKEN_EXPIRE_MINUTES`

## Rodando a API
```bash
uvicorn main:app --reload
```

A API fica disponível em:
- Swagger UI: http://127.0.0.1:8000/docs
- Endpoint raiz (homepage): http://127.0.0.1:8000/

## Autenticação
Autenticação via **JWT Bearer**.

### Obter token (login)
`POST /auth/login`

Body exemplo:
```json
{
  "email": "seu@email.com",
  "senha": "sua_senha"
}
```

Resposta:
```json
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "Bearer"
}
```

### Usar token nos endpoints protegidos
Envie o header:
```http
Authorization: Bearer SEU_ACCESS_TOKEN
```

## Endpoints

### Autenticação (`/auth`)
- `GET /auth/`
  - Descrição: rota padrão da autenticação.
- `POST /auth/criar_conta`
  - Descrição: cria um usuário.
- `POST /auth/login`
  - Descrição: autentica e retorna tokens.
- `POST /auth/login-form`
  - Descrição: autenticação via `application/x-www-form-urlencoded` (form OAuth2).
- `GET /auth/refresh`
  - Descrição: reemite access token com base no token atual.

### Pedidos (`/pedidos`)
- `GET /pedidos/`
  - Descrição: rota padrão de pedidos.
- `POST /pedidos/pedido`
  - Descrição: cria um pedido (status inicial: `PENDENTE`).
- `POST /pedidos/pedido/cancelar/{id_pedido}`
  - Descrição: cancela um pedido.
- `GET /pedidos/listar`
  - Descrição: lista todos os pedidos (somente admin).
- `POST /pedidos/pedido/adicionar-item/{id_pedido}`
  - Descrição: adiciona um item ao pedido e atualiza preço.
- `POST /pedidos/pedido/remover-item/{id_item_pedido}`
  - Descrição: remove um item e atualiza preço do pedido.
- `POST /pedidos/pedido/finalizar/{id_pedido}`
  - Descrição: finaliza um pedido.
- `GET /pedidos/pedido/{id_pedido}`
  - Descrição: visualiza um pedido.
- `GET /pedidos/listar/pedidos-usuario`
  - Descrição: lista pedidos do usuário autenticado.

## Como testar com cURL
1) Login:
```bash
curl -X POST http://127.0.0.1:8000/auth/login \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"seu@email.com\",\"senha\":\"sua_senha\"}"
```
2) Chamar um endpoint protegido:
```bash
curl http://127.0.0.1:8000/pedidos/ \
  -H "Authorization: Bearer SEU_ACCESS_TOKEN"
```

## Migrations (Alembic)
- Criar migração:
  ```bash
  alembic revision --autogenerate -m "mensagem"
  ```
- Aplicar migração:
  ```bash
  alembic upgrade head
  ```

> Observação: o setup do Alembic depende da configuração no `alembic.ini` e `alembic/env.py`.

## Licença
MIT

