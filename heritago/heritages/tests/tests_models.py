from django.test import TestCase
from heritages.models import Tag
from heritages.models import Heritage
from heritages.models import Multimedia
import os

testfile = "testfile.txt"
testfile2 = "testfile2.txt"


class ModelsTest(TestCase):
    def setUp(self):
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

    def tearDown(self):
        try:
            os.remove(testfile)
        except OSError:
            pass

        try:
            os.remove(testfile2)
        except OSError:
            pass

    def test_tag_initial(self):
        ancient_tag = Tag.objects.get(name="TAG_ancient")
        self.assertEqual(ancient_tag.name, "TAG_ancient")

    def test_heritage_create(self):
        """Try to get created heritage object.."""
        test_mosque = Heritage.objects.get(title="Test Mosque")
        self.assertEqual(test_mosque.title, "Test Mosque")

    def test_heritage_delete(self):
        """Try to get deleted heritage object.."""
        Heritage.objects.get(title="Test Mosque").delete()
        with self.assertRaises(Heritage.DoesNotExist):
            Heritage.objects.get(title="Test Mosque")

    def test_multimedia_delete(self):
        """Try to get deleted multimedia object.."""
        Multimedia.objects.get(url="A").delete()
        with self.assertRaises(Multimedia.DoesNotExist):
            Multimedia.objects.get(url="A")
