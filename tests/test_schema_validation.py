from playwright.sync_api import sync_playwright

from utils.schema_validator import validate_schema

BASE_URL = "https://restful-booker.herokuapp.com"


def test_auth_schema():

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

        response_data = response.json()

        validate_schema(
            response_data,
            "schemas/auth_schema.json"
        )

def test_booking_schema():

    payload = {
        "firstname": "Sahil",
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

        response_data = response.json()

        validate_schema(
            response_data,
            "schemas/booking_schema.json"
        )

def test_booking_list_schema():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.get(
            BASE_URL + "/booking"
        )

        response_data = response.json()

        validate_schema(
            response_data,
            "schemas/booking_list_schema.json"
        )