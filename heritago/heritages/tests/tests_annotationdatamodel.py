import unittest
from django.test import Client


class APITests(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_annotation_musthave_1ormore_contextproperty(self):
        self.assertEquals(1, 1)