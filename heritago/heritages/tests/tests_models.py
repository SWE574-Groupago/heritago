from django.test import TestCase
from heritages.models import Tag, Heritage, Multimedia

import os

testfile = "testfile.txt"
testfile2 = "testfile2.txt"


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        Tag.objects.create(name="TAG_ancient")
        title = "Test Mosque"
        Heritage.objects.create(title=title)
        file = open(testfile, "w")
        file.close()
        file = open(testfile2, "w")
        file.close()
        Multimedia.objects.create(url="B", file=testfile, heritage=Heritage.objects.get(title="Test Mosque"))
        Heritage.objects.create(title="Selimiye Mosque")
        Multimedia.objects.create(url="A", file=testfile2, heritage=Heritage.objects.get(title="Selimiye Mosque"))

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(testfile)
        except OSError:
            pass

        try:
            os.remove(testfile2)
        except OSError:
            pass

    def test_tag_get(self):
        ancient_tag = Tag.objects.get(name="TAG_ancient")
        self.assertEqual(ancient_tag.name, "TAG_ancient")

    def test_heritage_get(self):
        test_mosque = Heritage.objects.get(title="Test Mosque")
        self.assertEqual(test_mosque.title, "Test Mosque")

    def test_heritage_delete(self):
        Heritage.objects.get(title="Test Mosque").delete()
        with self.assertRaises(Heritage.DoesNotExist):
            Heritage.objects.get(title="Test Mosque")

    def test_multimedia_delete(self):
        Multimedia.objects.get(url="A").delete()
        with self.assertRaises(Multimedia.DoesNotExist):
            Multimedia.objects.get(url="A")
