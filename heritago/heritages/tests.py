from django.test import TestCase
from heritages.models import Tag
from heritages.models import Heritage
from heritages.models import Multimedia


class ModelsTest(TestCase):
    def setUp(self):
        Tag.objects.create(name="Osman")
        title = "Test Mosque"
        Heritage.objects.create(title=title)
        file = open("testfile.txt", "w")
        file.close()
        file = open("testfile2.txt", "w")
        file.close()
        Multimedia.objects.create(url = "B", file = "testfile.txt", heritage=Heritage.objects.get(title="Test Mosque"))
        Heritage.objects.create(title="Selimiye Mosque")
        Multimedia.objects.create(url = "A", file="testfile2.txt", heritage = Heritage.objects.get(title = "Selimiye Mosque"))

    def test_tag_initial(self):
        osmanTag = Tag.objects.get(name="Osman")
        self.assertEqual(osmanTag.name, "Osman")

    def test_heritage_create(self):
        """Try to get created heritage object.."""
        testMosq = Heritage.objects.get(title = "Test Mosque")
        self.assertEqual(testMosq.title, "Test Mosque")

    def test_heritage_delete(self):
        """Try to get deleted heritage object.."""
        Heritage.objects.get(title = "Test Mosque").delete()
        with self.assertRaises(Heritage.DoesNotExist):
            Heritage.objects.get(title="Test Mosque")

    def test_multimedia_delete(self):
        """Try to get deleted multimedia object.."""
        Multimedia.objects.get(url = "A").delete()
        with self.assertRaises(Multimedia.DoesNotExist):
            Multimedia.objects.get(url = "A")


import unittest
from django.test import Client


class APITests(unittest.TestCase):
    def setUp(self):
        """Creating a client"""
        self.client = Client()


