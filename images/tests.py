from django.test import TestCase
from .models import Category, Location, Image
import datetime as dt

class ImageTestClass(TestCase):
  def setUp(self):
    self.jeremy = Image(image_name='Jeremy', image_description='Jeremy is a Beast')

  def test_instance(self):
    self.assertTrue(isinstance(self.jeremy, Image))

  def test_save_instance(self):
    self.jeremy.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)

  def test_delete_instance(self):
    self.jeremy.save_image()
    self.jeremy.del_image()
    images = Image.objects.all()
    self.assertTrue(len(images) == 0)

  def test_get_images(self):
    self.jeremy.save_image()
    images = Image.get_image(1)
    self.assertTrue(len(images)>0)

  def test_get_all_images(self):
    self.jeremy.save_image()
    images = Image.all_images()
    self.assertTrue(len(images)>0)

  def tearDown(self):
    Editor.objects.all().delete()
    

class CategoryTestClass(TestCase):
  def setUp(self):
    self.jeremy = Category(Category='Jeremy')

  def test_instance(self):
    self.assertTrue(isinstance(self.jeremy, Category))

  def test_save_instance(self):
    self.jeremy.save_category()
    cats = Category.objects.all()
    self.assertTrue(len(cats)>0)

  def test_delete_instance(self):
    self.jeremy.save_category()
    self.jeremy.del_category()
    cats = Category.objects.all()
    self.assertTrue(len(cats) == 0)

class LocationTestClass(TestCase):
  def setUp(self):
    self.jeremy = Location(Location='Jeremy')

  def test_instance(self):
    self.assertTrue(isinstance(self.jeremy, Location))

  def test_save_instance(self):
    self.jeremy.save_location()
    locs = Category.objects.all()
    self.assertTrue(len(locs)>0)

  def test_delete_instance(self):
    self.jeremy.save_location()
    self.jeremy.del_location()
    locs = Location.objects.all()
    self.assertTrue(len(locs) == 0)