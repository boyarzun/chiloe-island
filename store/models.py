import uuid
import sys

# Django
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

# Models
from django.contrib.auth.models import User

#3rd parties
from ckeditor.fields import RichTextField
from io import BytesIO
from PIL import Image

def product_directory_path(instance, filename):
    """ File will be uploaded to MEDIA_ROOT/users/<user_id>/products/<product_id>/<filename> """
    ext = filename.split('.')[-1]
    name = uuid.uuid4()
    return f'users/{instance.seller_id}/products/{name}.{ext}'

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CommonInfo(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    old_price = models.PositiveIntegerField(blank=True, default=0)
    price = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        abstract = True

class Product(CommonInfo):
    categories = models.ManyToManyField(SubCategory)
    image_one = models.ImageField(upload_to=product_directory_path)
    image_two = models.ImageField(upload_to=product_directory_path, null=True, blank=True)
    image_three = models.ImageField(upload_to=product_directory_path, null=True, blank=True)
    image_four = models.ImageField(upload_to=product_directory_path, null=True, blank=True)
    description = RichTextField()

    def save(self, *args, **kwargs):

        if self.id:
            previous = Product.objects.get(pk=self.id)

            self.old_price = previous.price

        # Resizing images
        if not self.id:
            self.image_one = self.compressImage(self.image_one)
        else:
            if previous.image_one != self.image_one:
                self.image_one = self.compressImage(self.image_one)
        
        if self.image_two:
            if not self.id:
                self.image_two = self.compressImage(self.image_two)
            else:
                if previous.image_two != self.image_two:
                    self.image_two = self.compressImage(self.image_two)

        if self.image_three:
            if not self.id:
                self.image_three = self.compressImage(self.image_three)
            else:
                if previous.image_three != self.image_three:
                    self.image_three = self.compressImage(self.image_three)

        if self.image_four:
            if not self.id:
                self.image_four = self.compressImage(self.image_four)
            else:
                if previous.image_four != self.image_four:
                    self.image_four = self.compressImage(self.image_four)


        super(Product, self).save(*args, **kwargs)

    def compressImage(self, uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()

        if imageTemproary.width > 1000:
            resize_width = 1000
            (width, height) = (resize_width, (resize_width*imageTemproary.height)//imageTemproary.width)
        else:
            (width, height) = (imageTemproary.width, imageTemproary.height)

        imageTemproaryResized = imageTemproary.resize( (width,height) ) 
        imageTemproaryResized.save(outputIoStream , format='JPEG', quality=70)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage

    def __str__(self):
        return self.name

#class Service(CommonInfo):
#    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    