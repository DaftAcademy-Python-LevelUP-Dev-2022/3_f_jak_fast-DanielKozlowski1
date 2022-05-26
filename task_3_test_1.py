import unittest
import urllib.parse

import requests

from main import HerokuApp

EDGE_UA = "Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.58 Mobile Safari/537.36 EdgA/100.0.1185.50"


class HerokuSetupTest(unittest.TestCase):
    def setUp(self):
        self.app_path = urllib.parse.urljoin(HerokuApp.app_url, "/info")

    def test_json(self):
        response = requests.get(
            self.app_path, params={"format": "json"}, headers={"User-Agent": EDGE_UA}
        )
        self.assertEqual(response.json(), {"user_agent": EDGE_UA})


if __name__ == "__main__":
    unittest.main()
