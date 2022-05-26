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
        self.string_a = make_random_string()

    def test_put_200(self):
        response = requests.put(self.app_path + "/" + self.string_a)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
