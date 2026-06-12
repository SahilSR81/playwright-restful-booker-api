from playwright.sync_api import sync_playwright

BASE_URL = "https://restful-booker.herokuapp.com"


def test_generate_token():

    payload = {
        "username": "admin",
        "password": "password123"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.post(
            BASE_URL + "/auth",
            data=payload
        )

        assert response.status == 200

        response_data = response.json()

        assert "token" in response_data

        assert response_data["token"] is not None

        assert len(response_data["token"]) > 0

def test_wrong_username():

    payload = {
        "username": "wrongadmin",
        "password": "password123"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.post(
            BASE_URL + "/auth",
            data=payload
        )

        assert response.status == 200

        response_data = response.json()

        assert response_data["reason"] == "Bad credentials"

def test_wrong_password():

    payload = {
        "username": "admin",
        "password": "wrongpassword"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.post(
            BASE_URL + "/auth",
            data=payload
        )

        assert response.status == 200

        response_data = response.json()

        assert response_data["reason"] == "Bad credentials"

def test_empty_username():

    payload = {
        "username": "",
        "password": "password123"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.post(
            BASE_URL + "/auth",
            data=payload
        )

        response_data = response.json()

        assert response_data["reason"] == "Bad credentials"

def test_empty_password():

    payload = {
        "username": "admin",
        "password": ""
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.post(
            BASE_URL + "/auth",
            data=payload
        )

        response_data = response.json()

        assert response_data["reason"] == "Bad credentials"

def test_sql_injection_payload():

    payload = {
        "username": "' OR 1=1 --",
        "password": "' OR 1=1 --"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.post(
            BASE_URL + "/auth",
            data=payload
        )

        response_data = response.json()

        assert response_data["reason"] == "Bad credentials"

def test_xss_payload():

    payload = {
        "username": "<script>alert(1)</script>",
        "password": "<script>alert(1)</script>"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.post(
            BASE_URL + "/auth",
            data=payload
        )

        response_data = response.json()

        assert response_data["reason"] == "Bad credentials"

