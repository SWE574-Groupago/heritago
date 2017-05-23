import unittest
from django.test import Client

api_url = "/api/v1/annotations/"
domain = "http://heritago.com/"
annotation_id = ""


class AnnotationDataModelTests(unittest.TestCase):
    def setUp(self):
        self.Client = Client()

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
        annotation = [{
            '@context': 'http://www.w3.org/ns/anno.jsonld',
            'type': 'Annotation',
            'body': 'http://example.org/note1',
            'target': {
                'source': 'http://example.org/page1.html',
                'selector': {
                    'type': 'XPathSelector',
                    'value': '/html/body/p[2]/table/tr[2]/td[3]/span'
                }
            }
        }]

        response = self.Client.post(api_url, annotation).json()
        return response['id']

    def test_annotation_must_have_1_or_more_context_property(self):
        # TODO: code!: https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        """The Annotation must have 1 or more @context values and http://www.w3.org/ns/anno.jsonld must be one of them. If there is only one value, then it must be provided as a string. PROPERTY: @context)        """
        response = self.Client.get(annotation_id).json()
        self.assertTrue("@context" in response.keys())

    def test_an_annotation_must_have_exactly_1_IRI_that_defines_it(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        """An Annotation must have exactly 1 IRI that identifies it. PROPERTY: id"""
        response = self.Client.get(annotation_id).json()
        self.assertTrue("id" in response.keys())

    def test_an_annotation_must_have_1_or_more_types_and_the_annotation_class_must_be_one_of_them(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        """An Annotation must have 1 or more types, and the Annotation class must be one of them."""
        response = self.Client.get(annotation_id).json()
        self.assertTrue(response["type"], "Annotation")

    def test_there_should_be_1_or_more_body_relationships_associated_with_an_annotation_but_there_may_be_0(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        response = self.Client.get(annotation_id).json()
        self.assertTrue("body" in response.keys())
    
    def test_there_must_be_1_or_more_target_relationships_associated_with_an_annotation(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        response = self.Client.get(annotation_id).json()
        self.assertTrue("target" in response.keys())

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


@unittest.skipIf(False, 'Skipping tests that hit the real API server.')
def test_integration_contract():
    # Call the service to hit the actual API.
    actual = get_annotation()
    actual_keys = actual.json().pop().keys()

    # Call the service to hit the mocked API.
    with patch('requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        mocked = get_annotation()
        mocked_keys = mocked.json().pop().keys()

    # An object from the actual API and an object from the mocked API should have
    # the same data structure.


