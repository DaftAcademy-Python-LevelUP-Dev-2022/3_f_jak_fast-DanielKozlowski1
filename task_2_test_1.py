import unittest
import urllib.parse

import requests
from requests.auth import HTTPBasicAuth

from main import HerokuApp


class HerokuSetupTest(unittest.TestCase):
    def setUp(self):
        self.app_path = urllib.parse.urljoin(HerokuApp.app_url, "/check")

    def test_correct_age_200(self):
        response = requests.post(
            self.app_path, auth=HTTPBasicAuth(username="tester", password="1990-01-01")
        )
        self.assertEqual(response.status_code, 200)

    def test_incorrect_age_401(self):
        response = requests.post(
            self.app_path, auth=HTTPBasicAuth(username="tester", password="2022-01-01")
        )
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
