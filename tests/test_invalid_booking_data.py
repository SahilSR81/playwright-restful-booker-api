import pytest


@pytest.mark.parametrize(
    "firstname",
    [
        None,
        123,
        True,
        [],
        {}
    ]
)
def test_invalid_firstname_datatypes(
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