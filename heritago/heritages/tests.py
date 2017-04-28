from django.test import TestCase
from heritages.models import Tag

class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="Osman")

    def test_tag_initial(self):
        osmanTag = Tag.objects.get(name="Osman")
        self.assertEqual(osmanTag.name, "Osman")