import uuid

# Django
from django.conf import settings

# Models
from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    """ File will be uploaded to MEDIA_ROOT/<user_id>/<filename> """

    ext = filename.split('.')[-1]
    name = uuid.uuid4()
    return f'users/{instance.user.id}/{name}.{ext}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length = 50, null=True, verbose_name="Dirección")
    phone = models.CharField(max_length=18, null=True, verbose_name="Teléfono")
    avatar = models.ImageField(upload_to=user_directory_path, default='avatar/default.png')
    map = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return "Usuario: %s" % (self.user)
