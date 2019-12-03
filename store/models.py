import uuid

# Django
from django.db import models

# Models
from django.contrib.auth.models import User

#Ckeditor
from ckeditor.fields import RichTextField

def product_directory_path(instance, filename):
    """ File will be uploaded to MEDIA_ROOT/users/<user_id>/products/<product_id>/<filename> """
    ext = filename.split('.')[-1]
    name = uuid.uuid4()
    return f'users/{instance.seller_id}/products/{name}.{ext}'

class ProductCategory(models.Model):
    name = models.CharField(max_length=25)

class ProductSubCategory(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    categories = models.ManyToManyField(ProductSubCategory)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image_one = models.ImageField(upload_to=product_directory_path)
    image_two = models.ImageField(upload_to=product_directory_path, null=True)
    image_three = models.ImageField(upload_to=product_directory_path, null=True)
    active = models.BooleanField()
    description = RichTextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)