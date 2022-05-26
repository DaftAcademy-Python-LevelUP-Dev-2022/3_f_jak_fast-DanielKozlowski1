import datetime
import random
import string
import unittest
import urllib.parse

import requests

from main import HerokuApp


def make_random_string():
    return "".join(random.sample(string.ascii_lowercase, 10)) + "".join(
        str(random.randint(0, 8999))
    )


class HerokuSetupTest(unittest.TestCase):
    def setUp(self):
        self.app_path = urllib.parse.urljoin(HerokuApp.app_url, "/save")

    def test_get_404(self):
        response = requests.get(self.app_path + "/" + make_random_string())
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
