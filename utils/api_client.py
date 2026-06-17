from playwright.sync_api import sync_playwright


class APIClient:

    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self):

        self.playwright = sync_playwright().start()

        self.request_context = (
            self.playwright.request.new_context()
        )

    def get(self, endpoint):

        return self.request_context.get(
            self.BASE_URL + endpoint
        )

    def post(self, endpoint, payload):

        return self.request_context.post(
            self.BASE_URL + endpoint,
            data=payload
        )

    def put(self, endpoint, payload, headers=None):

        return self.request_context.put(
            self.BASE_URL + endpoint,
            data=payload,
            headers=headers
        )

    def delete(self, endpoint, headers=None):

        return self.request_context.delete(
            self.BASE_URL + endpoint,
            headers=headers
        )

    def close(self):

        self.request_context.dispose()

        self.playwright.stop()