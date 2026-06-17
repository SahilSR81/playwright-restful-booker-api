import pytest


@pytest.mark.parametrize(
    "username,password",
    [
        ("wrongadmin", "password123"),
        ("admin", "wrongpassword"),
        ("", "password123"),
        ("admin", ""),
    ]
)
def test_invalid_auth(
        api_client,
        username,
        password
):

    payload = {
        "username": username,
        "password": password
    }

    response = api_client.post(
        "/auth",
        payload
    )

    assert response.status == 200

    response_data = response.json()

    assert response_data["reason"] == (
        "Bad credentials"
    )