import unittest
import urllib.parse

import requests
from requests.auth import HTTPBasicAuth

from main import HerokuApp


class HerokuSetupTest(unittest.TestCase):
    def setUp(self):
        self.app_path = urllib.parse.urljoin(HerokuApp.app_url, "/check")

    def test_correct_age_correct_message(self):
        response = requests.post(
            self.app_path, auth=HTTPBasicAuth(username="tester", password="2000-01-01")
        )
        self.assertIn(
            "text/html",
            response.headers["Content-Type"],
        )
        self.assertIn(
            "<h1>Welcome tester! You are 22</h1>",
            response.content.decode(),
        )


if __name__ == "__main__":
    unittest.main()
