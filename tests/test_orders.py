def test_remove_missing_order_item_returns_400(client, test_user):
    login_response = client.post(
        "/auth/login",
        json={
            "email": "test@example.com",
            "senha": "test123",
        },
    )

    token = login_response.json()["access_token"]

    response = client.post(
        "/pedidos/pedido/remover-item/999999",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Item no pedido não existente"
    }
