import pytest


@pytest.mark.parametrize(
    "firstname",
    [
        "",
        "A",
        "A" * 255,
        "A" * 500
    ]
)
def test_create_booking_boundary_values(
        api_client,
        firstname
):

    payload = {
        "firstname": firstname,
        "lastname": "Kumar",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-05"
        }
    }

    response = api_client.post(
        "/booking",
        payload
    )

    print(response.status)