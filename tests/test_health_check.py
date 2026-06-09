import time
from playwright.sync_api import sync_playwright

BASE_URL = "https://restful-booker.herokuapp.com"

def test_ping_endpoint():
    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.get(BASE_URL+"/ping")

        assert response.status == 201
        assert response.ok

def test_response_time():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        start_time = time.time()

        response = request_context.get(
            BASE_URL + "/ping"
        )

        end_time = time.time()

        response_time = (end_time - start_time) * 1000

        assert response.status == 201

        assert response_time < 2000, (f"Response time too high: {response_time:.2f} ms")

def test_get_booking_ids():
    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.get(BASE_URL+"/booking")

        assert response.status == 200

        data = response.json()

        data = response.json()

        assert data is not None
        assert isinstance(data, list)
        assert len(data) > 0

def test_invalid_endpoint():
    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.get(
            BASE_URL + "/abcxyz"
        )

        assert response.status == 404

def test_wrong_http_method():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.post(
            BASE_URL + "/ping"
        )

        assert response.status in [404, 405]

