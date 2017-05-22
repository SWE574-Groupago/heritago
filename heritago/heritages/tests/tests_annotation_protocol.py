import unittest
from django.test import Client


class AnnotationProtocolTests(unittest.TestCase):
    def setUp(self):
        self.client = Client()

"""
https://www.w3.org/TR/annotation-protocol/

Cases to be tested (MUSTs:):

The Annotation Server must support the following HTTP methods on the Annotation's IRI:
1- GET (retrieve the description of the Annotation),
2- HEAD (retrieve the headers of the Annotation without an entity-body),
3- OPTIONS (enable CORS pre-flight requests [cors]).

4- Servers must support the JSON-LD representation using the Web Annotation profile. 
    These responses must have a Content-Type header with the application/ld+json media type
5- The response from the Annotation Server must have a Link header entry 
    where the target IRI is http://www.w3.org/ns/ldp#Resource and the rel parameter value is type.
6- For HEAD and GET requests, the response must have an ETag header with an entity reference value 
    that implements the notion of entity tags from HTTP [rfc7232]. 
    This value will be used by the client when sending update or delete requests.
7- The response must have an Allow header that lists the HTTP methods available 
    for interacting with the Annotation [rfc7231].


"""