from django.db import models
import datetimeas as dt

class Category(models.Model):
  category = models.TextField()

  def __str__(self):
    return self.category

class Location(models.Model):
  location = models.TextField()

  def __str__(self):
    return self.location

class Image(models.Model):
  image = models.ImageField(upload_to = 'photos')
  image_name = models.CharField(max_length=60)
  image_description = models.TextField()
  category = models.ForeignKey(Category)
  location = models.ForeignKey(Location)

  def __str__(self):
    return self.image_name

