import unittest
from django.test import Client


class AnnotationDataModelTests(unittest.TestCase):
    api_url_template = "/api/v1/heritages/#/annotations"
    xpath_annotation_response = ""

    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpClass(cls):
        cls.heritagePath = '/api/v1/heritages/'
        # super(AnnotationDataModelTests, cls).setUpClass()
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

    """ 
    EXAMPLE 22: XPath Selector
       {
          "@context": "http://www.w3.org/ns/anno.jsonld",
          "id": "http://example.org/anno22",
          "type": "Annotation",
          "body": "http://example.org/note1",
          "target": {
            "source": "http://example.org/page1.html",
            "selector": {
              "type": "XPathSelector",
              "value": "/html/body/p[2]/table/tr[2]/td[3]/span"
            }
          }
        }
    """

    def test_create_XPATH_annotation(self):
        """XPATH annotation created."""
        ann_id = self.create_XPATH_annotation()
        self.assertTrue(len(ann_id) > 0)

    def test_annotation_must_have_1_or_more_context_property(self):
        # TODO: code!: https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        """The Annotation must have 1 or more @context values and http://www.w3.org/ns/anno.jsonld must be one of them. If there is only one value, then it must be provided as a string. PROPERTY: @context)"""
        self.assertTrue("@context" in self.ann_get_response.keys())


    def test_an_annotation_must_have_exactly_1_IRI_that_defines_it(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        """An Annotation must have exactly 1 IRI that identifies it. PROPERTY: id"""
        self.assertTrue("id" in self.ann_get_response.keys())

    def test_an_annotation_must_have_1_or_more_types_and_the_annotation_class_must_be_one_of_them(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        """An Annotation must have 1 or more types, and the Annotation class must be one of them."""
        self.assertTrue(self.ann_get_response["type"], "Annotation")

    def test_there_should_be_1_or_more_body_relationships_associated_with_an_annotation_but_there_may_be_0(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        # response = self.client.get(self.__class__.annotation_id).json()
        self.assertTrue("body" in self.ann_get_response.keys())
    
    def test_there_must_be_1_or_more_target_relationships_associated_with_an_annotation(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        # response = self.client.get(annotation_id).json()
        self.assertTrue("target" in self.ann_get_response.keys())


