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
        "lastname": "Singh",
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
    
def test_update_booking():

    booking_id = create_booking()

    token = get_auth_token()

    payload = {
        "firstname": "Updated",
        "lastname": "User",
        "totalprice": 2000,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-02-01",
            "checkout": "2026-02-10"
        },
        "additionalneeds": "Lunch"
    }

    headers = {
        "Cookie": f"token={token}"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.put(
            BASE_URL + f"/booking/{booking_id}",
            data=payload,
            headers=headers
        )

        assert response.status == 200

        response_data = response.json()

        assert response_data["firstname"] == payload["firstname"]

        assert response_data["lastname"] == payload["lastname"]

        assert response_data["totalprice"] == payload["totalprice"]

def test_update_invalid_booking_id():

    token = get_auth_token()

    payload = {
        "firstname": "Test"
    }

    headers = {
        "Cookie": f"token={token}"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.put(
            BASE_URL + "/booking/99999999",
            data=payload,
            headers=headers
        )

        assert response.status == 400, (f"Expected 400 but got {response.status}")

def test_update_without_token():

    booking_id = create_booking()

    payload = {
        "firstname": "Updated"
    }

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.put(
            BASE_URL + f"/booking/{booking_id}",
            data=payload
        )

        assert response.status == 403
