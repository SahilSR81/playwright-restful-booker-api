from playwright.sync_api import sync_playwright

BASE_URL = "https://restful-booker.herokuapp.com"

def get_auth_token():

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

        return response.json()["token"]
    
def create_booking():

    payload = {
        "firstname": "Sahil",
        "lastname": "Kumar",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-05"
        },
        "additionalneeds": "Breakfast"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.post(
            BASE_URL + "/booking",
            data=payload
        )

        return response.json()["bookingid"]
    
def test_delete_booking():

    booking_id = create_booking()

    token = get_auth_token()

    headers = {
        "Cookie": f"token={token}"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.delete(
            BASE_URL + f"/booking/{booking_id}",
            headers=headers
        )

        assert response.status == 201

def test_verify_deleted_booking():

    booking_id = create_booking()

    token = get_auth_token()

    headers = {
        "Cookie": f"token={token}"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        delete_response = request_context.delete(
            BASE_URL + f"/booking/{booking_id}",
            headers=headers
        )

        assert delete_response.status == 201

        get_response = request_context.get(
            BASE_URL + f"/booking/{booking_id}"
        )

        assert get_response.status == 404

def test_delete_already_deleted_booking():

    booking_id = create_booking()

    token = get_auth_token()

    headers = {
        "Cookie": f"token={token}"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        first_delete = request_context.delete(
            BASE_URL + f"/booking/{booking_id}",
            headers=headers
        )

        assert first_delete.status == 201

        second_delete = request_context.delete(
            BASE_URL + f"/booking/{booking_id}",
            headers=headers
        )

        print(second_delete.status)
        print(second_delete.text())

def test_delete_invalid_booking_id():

    token = get_auth_token()

    headers = {
        "Cookie": f"token={token}"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.delete(
            BASE_URL + "/booking/99999999",
            headers=headers
        )

        print(response.status)
        print(response.text())

def test_delete_without_token():

    booking_id = create_booking()

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.delete(
            BASE_URL + f"/booking/{booking_id}"
        )

        assert response.status == 403

