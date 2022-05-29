from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):
    '''
        Set up method
    '''
    def setUp(self):
        self.london= Location(name='London')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.london, Location))