from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def update_location(self,name):
        Location.objects.filter(pk=self.pk).update(name=name)

    def delete_location(self):
        Location.objects.filter(pk=self.pk).delete()

class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def update_category(self,name):
        Category.objects.filter(pk=self.pk).update(name=name)

    def delete_category(self):
        Category.objects.filter(pk=self.pk).delete()

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/', null=True)
    image_name = models.CharField(max_length=50)
    image_description = models.CharField(max_length=255)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def update_image(self,image_name):
        Image.objects.filter(pk=self.pk).update(image_name__image_name=image_name)

    def delete_image(self):
        Image.objects.filter(pk=self.pk).delete()

    @classmethod
    def get_image_by_id(self):
        Image.objects.get(id=self.id)

    @classmethod
    def filter_by_location(self,image_location):
        Image.objects. filter(image_location__name=image_location)

    @classmethod
    def search_images_by_category(cls,images_category):
        images = cls.objects.filter(image_category__name = images_category)
        return images
