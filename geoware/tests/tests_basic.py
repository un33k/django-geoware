from django.conf import settings
from django.test import TestCase


class BasicTestCase(TestCase):
    """
    Geoware Basic Test
    """

    def test_basic(self):
        self.assertEqual(1, 1)
