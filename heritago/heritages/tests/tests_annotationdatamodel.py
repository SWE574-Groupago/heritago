import unittest
from django.test import Client


class AnnotationDataModelTests(unittest.TestCase):
    api_url_template = "/api/v1/heritages/#/annotations"
    xpath_annotation_response = ""

    @classmethod
    def setUpClass(cls):
        cls.heritagePath = '/api/v1/heritages/'
        h_id = cls.create_heritage_item()
        cls.api_url_set = cls.api_url_template.replace("#", str(h_id))
        cls.ann_response = cls.create_XPATH_annotation()
        cls.ann_id = cls.ann_response["id"].rsplit('/', 2)[-2]
        cls.ann_get_response = Client().get(cls.api_url_set + '/' + str(cls.ann_id)).json()

    @classmethod
    def create_heritage_item(cls):
        client = Client()
        r = client.post(cls.heritagePath, {
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
        return r.json()['id']

    @classmethod
    def create_XPATH_annotation(cls):
        return Client().post(cls.api_url_set, {
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
        }).json()

    def test_create_XPATH_annotation(self):
        ann_id = self.create_XPATH_annotation()
        self.assertTrue(len(ann_id) > 0)

    def test_annotation_must_have_1_or_more_context_property(self):
        self.assertTrue("@context" in self.ann_get_response.keys())

    def test_an_annotation_must_have_exactly_1_IRI_that_defines_it(self):
        self.assertTrue("id" in self.ann_get_response.keys())

    def test_an_annotation_must_have_1_or_more_types_and_the_annotation_class_must_be_one_of_them(self):
        self.assertTrue(self.ann_get_response["type"], "Annotation")

    def test_an_annotation_must_have_body_relationships_associated_with_it(self):
        self.assertTrue("body" in self.ann_get_response.keys())
    
    def test_there_must_be_1_or_more_target_relationships_associated_with_an_annotation(self):
        self.assertTrue("target" in self.ann_get_response.keys())


