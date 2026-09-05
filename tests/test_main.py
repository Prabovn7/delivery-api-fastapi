from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_homepage():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["mensagem"] == "Bem-vindo à Delivery FastAPI!"
    assert data["docs"] == "/docs"
    assert data["redoc"] == "/redoc"
    assert data["auth"] == "/auth/"
    assert data["pedidos"] == "/pedidos/"


def test_auth_home():
    response = client.get("/auth/")

    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "Você acessou a rota padrão de autenticação",
        "autenticado": False,
    }


def test_orders_requires_authentication():
    response = client.get("/pedidos/")

    assert response.status_code == 401
