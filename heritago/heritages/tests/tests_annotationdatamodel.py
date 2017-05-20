import unittest
from django.test import Client


class AnnotationDataModelTests(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    """
    EXAMPLE 1: Basic Annotation Model
    {
      "@context": "http://www.w3.org/ns/anno.jsonld",
      "id": "http://example.org/anno1",
      "type": "Annotation",
      "body": "http://example.org/post1",
      "target": "http://example.com/page1"
    }
    """

    def test_annotation_must_have_1_or_more_context_property(self):
        # TODO: code!: https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        """The Annotation must have 1 or more @context values and http://www.w3.org/ns/anno.jsonld must be one of them. If there is only one value, then it must be provided as a string. PROPERTY: @context)        """
        raise NotImplementedError

    def test_an_annotation_must_have_exactly_1_IRI_that_defines_it(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        """An Annotation must have exactly 1 IRI that identifies it. PROPERTY: id"""
        raise NotImplementedError

    def test_an_annotation_must_have_1_or_more_types_and_the_annotation_class_must_be_one_of_them(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        """An Annotation must have 1 or more types, and the Annotation class must be one of them."""
        raise NotImplementedError

    def test_there_should_be_1_or_more_body_relationships_associated_with_an_annotation_but_there_may_be_0(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        raise NotImplementedError
    
    def test_there_must_be_1_or_more_target_relationships_associated_with_an_annotation(self):
        # TODO: code! https://www.w3.org/TR/annotation-model/ 3.1 Annotations Example-1
        raise NotImplementedError

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

