from jose import jwt

from config import SECRET_KEY, ALGORITHM


def test_login_success(client, test_user):
    response = client.post(
        "/auth/login",
        json={
            "email": "test@example.com",
            "senha": "test123",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "Bearer"

    payload = jwt.decode(
        data["access_token"],
        SECRET_KEY,
        algorithms=[ALGORITHM],
    )

    assert payload["sub"] == str(test_user.id)


def test_login_invalid_password(client, test_user):
    response = client.post(
        "/auth/login",
        json={
            "email": "test@example.com",
            "senha": "wrong-password",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Usuário não encontrado ou credenciais inválidas"
    )


def test_authenticated_user_can_access_orders(client, test_user):
    login_response = client.post(
        "/auth/login",
        json={
            "email": "test@example.com",
            "senha": "test123",
        },
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/pedidos/",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "Você acessou a rota de pedidos"
    }
