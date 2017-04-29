import unittest
from django.test import Client


class APITests(unittest.TestCase):
    def setUp(self):
        """Creating a client"""
        self.client = Client()

    def test_heritages_endpoint_upandrunning(self):
        # TODO: Find a more generic way, path changes must not affect tests
        response = self.client.get('/api/v1/heritages/')
        self.assertEqual(response.status_code, 200)

    def test_heritages_post_heritage(self):
        self.client.post()