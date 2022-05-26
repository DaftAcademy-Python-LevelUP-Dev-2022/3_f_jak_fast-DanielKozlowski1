import unittest
import urllib.parse

import requests

from main import HerokuApp

EDGE_UA = "Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.58 Mobile Safari/537.36 EdgA/101.0.1185.50"


class HerokuSetupTest(unittest.TestCase):
    def setUp(self):
        self.app_path = urllib.parse.urljoin(HerokuApp.app_url, "/info")

    def test_html(self):
        response = requests.get(
            self.app_path, params={"format": "html"}, headers={"User-Agent": EDGE_UA}
        )
        self.assertIn(
            f'<input type="text" id=user-agent name=agent value="{EDGE_UA}">',
            response.content.decode(),
        )

    def test_incorrect_format(self):
        response = requests.get(
            self.app_path, params={"format": "aujfdhs"}, headers={"User-Agent": EDGE_UA}
        )
        self.assertEqual(response.status_code, 400)

    def test_no_format(self):
        response = requests.get(self.app_path, headers={"User-Agent": EDGE_UA})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
