from django.db import models
import datetime as dt

class Category(models.Model):
  category = models.TextField()

  def save_category(self):
    self.save()

  def del_category(self):
    self.delete()

  def __str__(self):
    return self.category

class Location(models.Model):
  location = models.TextField()

  def save_location(self):
    self.save()

  def del_location(self):
    self.delete()

  def __str__(self):
    return self.location

class Image(models.Model):
  image = models.ImageField(upload_to = 'photos/')
  image_name = models.CharField(max_length=60)
  image_description = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  category = models.ManyToManyField(Category)
  location = models.ForeignKey(Location)

  def save_image(self):
    self.save()

  def del_image(self):
    self.delete()

  def get_image(self, id):
    image = Image.objects.get(pk=id)
    return image

  def update_image(self, id, updated_name):
    image = Image.objects.filter(pk=id).update(image_name=updated_name)
    return image.save_image()

  @classmethod
  def all_images(cls):
    images = cls.objects.all()
    return images

  @classmethod
  def search_image(cls, search):
    image = cls.objects.filter(category__category__icontains=search)
    return image

  @classmethod
  def filter_images(cls, place):
    images = cls.objects.filter(location__location=place)
    return images

  def __str__(self):
    return self.image.url

