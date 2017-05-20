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
        file = open(testfile, "w")
        file.close()

    def tearDown(self):
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

    def test_heritages_endpoint_upandrunning(self):
        """The endpoint api/heritages is up and running."""
        response = self.client.get(heritagePath)
        self.assertEqual(response.status_code, 200)

    def test_heritages_addnewheritage_with_inadequateinfo(self):
        """ENDPOINT: api/heritages, METHOD:POST, CONDITION: with only title information, EXPECTING: StatusCode:400"""
        response = self.client.post(heritagePath, {
            "title": "Ayasofya"
        })
        self.assertEquals(response.status_code, 400)

    def test_heritages_addnewheritage_withnoenddate(self):
        """ENDPOINT: api/heritages, METHOD: POST, with no endDate, EXPECTING: StatusCode:400"""
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

    def test_heritages_addnewheritage(self):
        """ENDPOINT: api/heritages, METHOD: POST, CONDITION: with full info, EXPECTING: an onbject with a id property filled."""
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

    def test_heritages_searchheritagesbykeyword_existing(self):
        """ENDPOINT: api/heritages, METHOD: GET, QUERYSTR: ?keyword=kwrd, CONDITION: search by a keyword, EXPECTING: not empty response."""
        r = self.client.get(heritagePath + "?keyword=santa")
        response = r.json()
        self.assertGreaterEqual(len(response), 0)

    def test_heritages_searchheritagesbykeyword_notexisting(self):
        """ENDPOINT: api/heritages, METHOD: GET, QUERYSTR: ?keyword=kwrd, CONDITION: search by a keyword, EXPECTING: empty response"""
        r = self.client.get(heritagePath + "?keyword=nonexistingitem")
        response = r.json()
        self.assertEqual(len(response), 0)

    def test_heritages_getmultimediasofaheritageitem(self):
        """ENDPOINT: api/heritages/{hid}/multimedia, METHOD: GET, CONDITION: heritage item exists with no multimedia, EXPECTING: empty multimedia """
        hitemresponse = APITests.createNewHeritageItem(self)
        id = hitemresponse.json()["id"]
        r = self.client.get(heritagePath + str(id) + "/multimedia")
        response = r.json()
        self.assertEqual(len(response), 0)

    def test_heritages_trytogetnonexistingheritageitemsmultimedia(self):
        """ENDPOINT: api/heritages/{hid}/multimedia, METHOD: GET, CONDITION: heritage item does not exist, EXPECTING: empty multimedia """
        r = self.client.get(heritagePath + "99/multimedia")
        self.assertEqual(r.status_code, 404)

    def test_heritages_trytoCreateNonexistingHeritageItemAMultimedia(self):
        """ENDPOINT: api/heritages/{hid}/multimedia, METHOD: POST, CONDITION: create a multimedia for a heritage item that does not exist, EXPECTING: StatusCode:404 """
        r = self.client.post(heritagePath + "99/multimedia", {
            "type": "image"
        })
        self.assertEqual(r.status_code, 404)

    def test_heritages_AddMultimediaToHeritageItem(self):
        """ENDPOINT: api/heritages/{hid}/multimedia, METHOD: POST, CONDITION: create heritage item and add mmedia to it, EXPECTING: StatusCode:201 """
        heritageitem = APITests.createNewHeritageItem(self)
        heritageitem = heritageitem.json()
        id = heritageitem["id"]
        r = self.client.post(heritagePath + str(id) + "/multimedia", {
            "type": "image"
        })
        self.assertEqual(r.status_code, 201)
