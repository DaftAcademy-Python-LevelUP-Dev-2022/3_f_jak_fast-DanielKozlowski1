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

    def test_put_get_redirect(self):
        response_put = requests.put(self.app_path + "/" + self.string_a)
        self.assertEqual(response_put.status_code, 200)
        response_get = requests.get(
            self.app_path + "/" + self.string_a, allow_redirects=False
        )
        self.assertEqual(response_get.status_code, 301)
        self.assertIn("info", response_get.headers["Location"])


if __name__ == "__main__":
    unittest.main()
