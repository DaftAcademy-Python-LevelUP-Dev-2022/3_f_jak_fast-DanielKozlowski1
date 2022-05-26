import unittest
import urllib.parse

import requests

from main import HerokuApp


class HerokuSetupTest(unittest.TestCase):
    def setUp(self):
        self.app_path = urllib.parse.urljoin(HerokuApp.app_url, "/start")
        self._response = requests.get(self.app_path)

    def test_url_exists(self):
        self.assertIsNotNone(HerokuApp.app_url)
        self.assertIsInstance(HerokuApp.app_url, str)
        self.assertNotEqual(HerokuApp.app_url, "")

    def test_status_code(self):
        self.assertEqual(self._response.status_code, 200)

    def test_content_type(self):
        self.assertIn("text/html", self._response.headers["Content-Type"])

    def test_response(self):
        self.assertIn(
            "<h1>The unix epoch started at 1970-01-01</h1>",
            self._response.content.decode(),
        )


if __name__ == "__main__":
    unittest.main()
