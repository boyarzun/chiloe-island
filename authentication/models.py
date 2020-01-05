import uuid

# Django
from django.template.defaultfilters import slugify
from django.conf import settings

# Models
from django.db import models
from django.contrib.auth.models import User

class Commune(models.Model):
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, verbose_name='Nombre slug')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Commune, self).save(*args, **kwargs)

def user_directory_path(instance, filename):
    """ File will be uploaded to MEDIA_ROOT/users/<user_id>/products/<filename> """

    ext = filename.split('.')[-1]
    name = uuid.uuid4()
    return f'users/{instance.user.id}/products/{name}.{ext}'

def cover_photo_directory_path(instance, filename):
    """ File will be uploaded to MEDIA_ROOT/users/<user_id>/cover/<filename> """

    ext = filename.split('.')[-1]
    name = uuid.uuid4()
    return f'users/{instance.user.id}/cover/{name}.{ext}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length = 50, null=True, verbose_name="Dirección")
    phone = models.CharField(max_length=18, null=True, verbose_name="Teléfono")
    avatar = models.ImageField(upload_to=user_directory_path, default='avatar/default.png')
    cover_photo = models.ImageField(upload_to=cover_photo_directory_path, null=True, blank=True)
    map = models.URLField(max_length=250, null=True, blank=True)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    terms_conditions= models.BooleanField(default=True)

    def __str__(self):
        return "Usuario: %s" % (self.user)

