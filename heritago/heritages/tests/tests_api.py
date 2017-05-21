import unittest
from django.test import Client

heritagePath = '/api/v1/heritages/'


class APITests(unittest.TestCase):
    def setUp(self):
        """Creating a client"""
        self.client = Client()

    def test_heritages_endpoint_upandrunning(self):
        response = self.client.get(heritagePath)
        self.assertEqual(response.status_code, 200)

    def test_heritages_addnewheritage_with_inadequateinfo(self):
        """POSTing with inadequate fields"""
        response = self.client.post(heritagePath, {
            "title": "Ayasofya"
        })
        print(response.status_code)
        self.assertEquals(response.status_code, 400)

    def test_heritages_addnewheritage_withnoenddate(self):
        """POSTing with no endDate"""
        response = self.client.post(heritagePath, {
            "title": "Helva",
            "description": "desc",
            "startDate": "500",
            "exactDate": "2000",
            "origin": [{"name": "Turkey"}, {"name": "Afghanistan"}],
            "basicInformation": [{"name": "AKA", "value": "Halawa"}],
            "tags": [{"name": "religion"}, {"name": "christmas"}, {"name": "figure"}]
        })
        # I could have add an item without endDate
        print("POST Heriatage With no endDate => response status code (*expecting 201): " + str(response.status_code))
        self.assertEqual(response.status_code, 201)

    def test_heritages_addnewheritage(self):
        """POSTing with full info"""
        r = self.client.post(heritagePath, {
            "title": "Santa Clause",
            "description": "Santa Claus, also known as Saint Nicholas, Saint Nick, Kris Kringle, Father Christmas, "
                           "or simply Santa (Santy in Hiberno-English), is a legendary figure of Western Christian "
                           "culture who is said to bring gifts to the homes of well-behaved (\"good\" or \"nice\") "
                           "children on Christmas Eve (24 December) and the early morning hours of Christmas Day "
                           "(25 December).",
            "startDate": "1087",
            "endDate": "continuing",
            "exactDate": "1700",
            "origin": [{"name": "Dutch"}, {"name": "British"}],
            "basicInformation": [{"name": "AKA", "value": "Sinterklaas"}],
            "tags": [{"name": "religion"}, {"name": "christmas"}, {"name": "figure"}]
        })
        response = r.json()
        print(response["id"])
        self.assertIsInstance(response["id"], int)
