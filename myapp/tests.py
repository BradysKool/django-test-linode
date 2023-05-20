from django.test import TestCase
from .models import Person

class PersonModleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.person = Person.objects.create(
            name = "mufuf",
            koolness = 9
        )
    
    def test_fiels(self):
        self.assertIsInstance(self.person.name, str)

        self.assertIsInstance(self.person.koolness, int)

