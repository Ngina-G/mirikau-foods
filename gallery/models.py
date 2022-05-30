from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/', null=True)
    image_name = models.CharField(max_length=50)
    image_description = models.CharField(max_length=255)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)