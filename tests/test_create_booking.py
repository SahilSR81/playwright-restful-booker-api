from playwright.sync_api import sync_playwright

BASE_URL = "https://restful-booker.herokuapp.com"


def test_create_booking():

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

        assert response.status == 200

        response_data = response.json()

        assert "bookingid" in response_data

        assert response_data["bookingid"] is not None

        assert response_data["booking"]["firstname"] == payload["firstname"]

        assert response_data["booking"]["lastname"] == payload["lastname"]

def test_create_booking_missing_firstname():

    payload = {
        "lastname": "Kumar",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-05"
        }
    }

    with sync_playwright() as p:
        request_context = p.request.new_context()

        response = request_context.post(
            BASE_URL + "/booking",
            data=payload
        )

        print(response.status)
        print(response.text())
