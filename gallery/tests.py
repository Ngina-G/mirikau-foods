from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):
    '''
        Set up method
    '''
    def setUp(self):
        self.london= Location(name='London')

    def tearDown(self):
        Location.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.london, Location))

    # Testing Save Method
    def test_save_method(self):
        self.london.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)> 0)

    def test_update_method(self):
        self.london.update_location(name='Berlin')
        self.assertTrue(self.london.name, 'Berlin')

    def test_delete_method(self):
        self.london.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)


class CategoryTestClass(TestCase):
    '''
        Set up method
    '''
    def setUp(self):
        self.food= Category(name='Food')

    def tearDown(self):
        Category.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food, Category))

    # Testing Save Method
    def test_save_method(self):
        self.food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)> 0)

    def test_update_method(self):
        # At this point self.food.name is still Food, but the value in the database
        # was updated to Drinks. The object's updated value needs to be reloaded
        # from the database.
        self.food.update_category(name='Drinks')
        self.assertTrue(self.food.name, 'Drinks')

    def test_delete_method(self):
        self.food.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)==0)

class ImageTestClass(TestCase):
    '''
        Set up
    '''

    def setUp(self):
        self.london= Location(name='London')
        self.london.save_location()

        self.food= Category(name='Food')
        self.food.save_category()

        self.new_image= Image(image_name='Bay pizza', image_description='Tasty pizzas are the best', image_location=self.london, image_category=self.food)
        self.new_image.save_image()

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_save_method(self):
        self.new_image= Image(image_name='Bay pizza', image_description='Tasty pizzas are the best', image_location=self.london, image_category=self.food)
        self.new_image.save_image()

    def test_update_method(self):
        self.new_image.update_image(image_name='Berlin')
        self.assertTrue(self.new_image.image_name, 'Berlin')

    def test_delete_method(self):
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    # def test_get_image_by_id(self):
    #     new