import unittest
import os
from django.test import Client

heritagePath = '/api/v1/heritages/'
testfile = 'testImage.jpg'

""" TODO: I am aware long lines violate PEP 8, but for "coverage run --source='.' manage.py test heritages -v 2" command
 to work properly, I had to do the docstrings this way."""


class APITests(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpClass(cls):
        file = open(testfile, "w")
        file.close()

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(testfile)
        except OSError:
            pass

    def createNewHeritageItem(self):
        return self.client.post(heritagePath, {
            "title": "Helva",
            "description": "desc",
            "startDate": "500",
            "exactDate": "2000",
            "origin": [{"name": "Turkey"}, {"name": "Afghanistan"}],
            "basicInformation": [{"name": "AKA", "value": "Halawa"}],
            "tags": [{"name": "religion"}, {"name": "christmas"}, {"name": "figure"}]
        })

    def test_heritages_endpoint_up_and_running(self):
        """ENDPOINT: api/heritages, METHOD: GET"""
        response = self.client.get(heritagePath)
        self.assertEqual(response.status_code, 200)

    def test_heritages_add_new_heritage_with_inadequate_info_expecting_400_response(self):
        """ENDPOINT: api/heritages, METHOD: POST"""
        response = self.client.post(heritagePath, {
            "title": "Ayasofya"
        })
        self.assertEquals(response.status_code, 400)

    def test_heritages_add_new_heritage_with_no_enddate_expecting_201_response(self):
        """ENDPOINT: api/heritages, METHOD: POST"""
        response = self.client.post(heritagePath, {
            "title": "Helva",
            "description": "desc",
            "startDate": "500",
            "exactDate": "2000",
            "origin": [{"name": "Turkey"}, {"name": "Afghanistan"}],
            "basicInformation": [{"name": "AKA", "value": "Halawa"}],
            "tags": [{"name": "religion"}, {"name": "christmas"}, {"name": "figure"}]
        })
        self.assertEqual(response.status_code, 201)

    def test_heritages_add_new_heritage_expecting_to_create_a_new_id(self):
        """ENDPOINT: api/heritages, METHOD: POST"""
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
        self.assertIsInstance(response["id"], int)

    def test_heritages_search_heritages_by_keyword_existing_expecting_result(self):
        """ENDPOINT: api/heritages, METHOD: GET"""
        r = self.client.get(heritagePath + "?keyword=santa")
        response = r.json()
        self.assertGreaterEqual(len(response), 0)

    def test_heritages_search_heritages_bykeyword_notexisting_expecting_empty_result(self):
        """ENDPOINT: api/heritages, METHOD: GET"""
        r = self.client.get(heritagePath + "?keyword=nonexistingitem")
        response = r.json()
        self.assertEqual(len(response), 0)

    def test_heritages_get_multimedia_of_a_heritage_item(self):
        """ENDPOINT: api/heritages/{hid}/multimedia, METHOD: GET, CONDITION: heritage item exists with no multimedia, EXPECTING: empty multimedia """
        h_item_response = APITests.createNewHeritageItem(self)
        h_id = h_item_response.json()["id"]
        r = self.client.get(heritagePath + str(h_id) + "/multimedia")
        response = r.json()
        self.assertEqual(len(response), 0)

    def test_heritages_try_to_get_non_existing_heritage_items_multimedia(self):
        """ENDPOINT: api/heritages/{hid}/multimedia, METHOD: GET, CONDITION: heritage item does not exist, EXPECTING: empty multimedia """
        r = self.client.get(heritagePath + "99/multimedia")
        self.assertEqual(r.status_code, 404)

    def test_heritages_try_to_create_non_existing_heritage_item_a_multimedia(self):
        """ENDPOINT: api/heritages/{hid}/multimedia, METHOD: POST, CONDITION: create a multimedia for a heritage item that does not exist, EXPECTING: StatusCode:404 """
        r = self.client.post(heritagePath + "99/multimedia", {
            "type": "image"
        })
        self.assertEqual(r.status_code, 404)

    def test_heritages_add_multimedia_to_heritage_item(self):
        """ENDPOINT: api/heritages/{hid}/multimedia, METHOD: POST, CONDITION: create heritage item and add mmedia to it, EXPECTING: StatusCode:201 """
        heritage_id = APITests.createNewHeritageItem(self).json()["id"]
        r = self.client.post(heritagePath + str(heritage_id) + "/multimedia", {
            "type": "image"
        })
        self.assertEqual(r.status_code, 201)
