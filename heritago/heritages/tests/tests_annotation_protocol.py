import unittest
from django.test import Client


class AnnotationProtocolTests(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpClass(cls):
        cls.heritagePath = '/api/v1/heritages/'
        client = Client()
        h_response = client.post(cls.heritagePath, {
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

        cls.anno = {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "type": "Annotation",
            "creator": "me",
            "body": [
                {
                    "type": "video",
                    "format": "text/plain",
                    "value": "loved it"
                }
            ],
            "target": [
                {
                    "type": "text",
                    "format": "text/plain",
                    "selector": [
                        {
                            "type": "FragmentSelector",
                            "conformsTo": "http://tools.ietf.org/rfc/rfc5147",
                            "value": "char=2,4"
                        }
                    ]
                }
            ]
        }

        cls.heritage_id = h_response.json()["id"]
        cls.annotation_path = "/api/v1/heritages/" + str(cls.heritage_id) + "/annotations"

    def test_protocol_response_must_have_an_allow_header_that_lists_the_HTTP_methods_available(self):
        response = self.client.post(self.annotation_path, self.anno)
        self.assertTrue(len(response["Allow"]) > 0)
        self.assertTrue("GET" in response["Allow"])
        self.assertTrue("POST" in response["Allow"])
        self.assertTrue("HEAD" in response["Allow"])
        self.assertTrue("OPTIONS" in response["Allow"])

    def test_GET_retrieve_the_description_of_the_Annotation(self):
        self.client.post(self.annotation_path, self.anno)
        response = self.client.get(self.annotation_path, self.anno)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_HEAD_retrieve_the_headers_of_the_Annotation_without_an_entitybody(self):
        response = self.client.head(self.annotation_path)
        self.assertEqual(response.status_code, 200)

    def test_OPTIONS_is_CORS_preflight_requests_enabled(self):
        response = self.client.options(self.annotation_path)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
        
    def test_responses_must_have_a_ContentType_header_with_the_application_ldjson_media_type(self):
        response_post = self.client.post(self.annotation_path, self.anno)["Content-Type"]
        response_get = self.client.get(self.annotation_path, self.anno)["Content-Type"]
        response_head = self.client.head(self.annotation_path)["Content-Type"]
        response_options = self.client.options(self.annotation_path)["Content-Type"]
        expected_content_type = "application/ld+json; profile=\"http://www.w3.org/ns/anno.jsonld\""
        self.assertEqual(expected_content_type, response_post, "POST")
        self.assertEqual(expected_content_type, response_get, "GET")
        self.assertEqual(expected_content_type, response_head, "HEAD")
        self.assertEqual(expected_content_type, response_options, "OPTIONS")

    def test_response_must_have_a_Link_header_entry_and_contains_rel_type(self):
        self.client.post(self.annotation_path, self.anno)
        response = self.client.get(self.annotation_path, self.anno)
        try:
            response["Link"]
            self.assertTrue("rel=\"type\"" in response["Link"])
        except KeyError:
            self.fail("Annotation response does not contain \"Link\" header")

    def test_HEAD_and_GET_requests_response_must_have_an_ETag_header_with_an_entity_reference_value(self):
        self.client.post(self.annotation_path, self.anno)
        response_get = self.client.get(self.annotation_path, self.anno)
        response_head = self.client.head(self.annotation_path)
        self.assertTrue("ETag" in response_get)
        self.assertTrue("ETag" in response_head)
