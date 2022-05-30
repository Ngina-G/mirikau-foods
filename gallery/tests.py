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

    # Testing Save Method
    def test_save_method(self):
        self.london.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)> 0)

    # def test_delete_method(self):
    #     self.london.delete_location(id)
    #     locations = Location.objects.all()
    #     self.assertTrue(len(locations)< 0)

class CategoryTestClass(TestCase):
    '''
        Set up method
    '''
    def setUp(self):
        self.food= Category(name='Food')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food, Category))

    # Testing Save Method
    def test_save_method(self):
        self.food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)> 0)

