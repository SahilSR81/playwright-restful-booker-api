from playwright.sync_api import sync_playwright

from utils.logger import logger


class APIClient:

    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self):

        self.playwright = sync_playwright().start()

        self.request_context = (
            self.playwright.request.new_context()
        )

    def get(self, endpoint):

        logger.info("=" * 80)

        logger.info(
            f"GET REQUEST -> {endpoint}"
        )

        try:

            response = self.request_context.get(
                self.BASE_URL + endpoint,
                timeout=5000
            )

            logger.info(
                f"STATUS CODE -> {response.status}"
            )

            logger.info(
                f"RESPONSE BODY -> {response.text()}"
            )

            return response

        except Exception as e:

            logger.error(
                f"GET REQUEST FAILED -> {str(e)}"
            )

            raise

    def post(self, endpoint, payload):

        logger.info("=" * 80)

        logger.info(
            f"POST REQUEST -> {endpoint}"
        )

        logger.info(
            f"REQUEST BODY -> {payload}"
        )

        try:

            response = self.request_context.post(
                self.BASE_URL + endpoint,
                data=payload,
                timeout=5000
            )

            logger.info(
                f"STATUS CODE -> {response.status}"
            )

            logger.info(
                f"RESPONSE BODY -> {response.text()}"
            )

            return response

        except Exception as e:

            logger.error(
                f"POST REQUEST FAILED -> {str(e)}"
            )

            raise

    def put(
            self,
            endpoint,
            payload,
            headers=None
    ):

        logger.info("=" * 80)

        logger.info(
            f"PUT REQUEST -> {endpoint}"
        )

        logger.info(
            f"REQUEST BODY -> {payload}"
        )

        logger.info(
            f"HEADERS -> {headers}"
        )

        try:

            response = self.request_context.put(
                self.BASE_URL + endpoint,
                data=payload,
                headers=headers,
                timeout=5000
            )

            logger.info(
                f"STATUS CODE -> {response.status}"
            )

            logger.info(
                f"RESPONSE BODY -> {response.text()}"
            )

            return response

        except Exception as e:

            logger.error(
                f"PUT REQUEST FAILED -> {str(e)}"
            )

            raise

    def patch(
            self,
            endpoint,
            payload,
            headers=None
    ):

        logger.info("=" * 80)

        logger.info(
            f"PATCH REQUEST -> {endpoint}"
        )

        logger.info(
            f"REQUEST BODY -> {payload}"
        )

        logger.info(
            f"HEADERS -> {headers}"
        )

        try:

            response = self.request_context.patch(
                self.BASE_URL + endpoint,
                data=payload,
                headers=headers,
                timeout=5000
            )

            logger.info(
                f"STATUS CODE -> {response.status}"
            )

            logger.info(
                f"RESPONSE BODY -> {response.text()}"
            )

            return response

        except Exception as e:

            logger.error(
                f"PATCH REQUEST FAILED -> {str(e)}"
            )

            raise

    def delete(
            self,
            endpoint,
            headers=None
    ):

        logger.info("=" * 80)

        logger.info(
            f"DELETE REQUEST -> {endpoint}"
        )

        logger.info(
            f"HEADERS -> {headers}"
        )

        try:

            response = self.request_context.delete(
                self.BASE_URL + endpoint,
                headers=headers,
                timeout=5000
            )

            logger.info(
                f"STATUS CODE -> {response.status}"
            )

            logger.info(
                f"RESPONSE BODY -> {response.text()}"
            )

            return response

        except Exception as e:

            logger.error(
                f"DELETE REQUEST FAILED -> {str(e)}"
            )

            raise

    def close(self):

        self.request_context.dispose()

        self.playwright.stop()