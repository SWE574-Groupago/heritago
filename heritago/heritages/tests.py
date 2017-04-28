from django.test import TestCase
from heritages.models import Tag
from heritages.models import Heritage

class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="Osman")
        title = "Test Mosque"
        Heritage.objects.create(title=title)

    def test_tag_initial(self):
        osmanTag = Tag.objects.get(name="Osman")
        self.assertEqual(osmanTag.name, "Osman")

# class HeritageTestCase(TestCase):
    def test_heritage_create(self):
        """Try to get created heritage object.."""
        testMosq = Heritage.objects.get(title = "Test Mosque")
        self.assertEqual(testMosq.title, "Test Mosque")

    def test_heritage_delete(self):
        """Try to get deleted heritage object.."""
        Heritage.objects.get(title = "Test Mosque").delete()
        with self.assertRaises(Heritage.DoesNotExist):
            Heritage.objects.get(title="Test Mosque")
