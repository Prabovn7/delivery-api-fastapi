from fastapi import FastAPI

from auth_routes import auth_router
from order_routes import order_router

app = FastAPI(
    title="Delivery FastAPI",
    description="API de autenticação (JWT) e pedidos.",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(order_router)


@app.get(
    "/",
    tags=["home"],
    summary="Homepage da API",
    description="Página inicial com links para a documentação e rotas principais.",
)
async def homepage():
    return {
        "mensagem": "Bem-vindo à Delivery FastAPI!",
        "docs": "/docs",
        "redoc": "/redoc",
        "auth": "/auth/",
        "pedidos": "/pedidos/",
    }
