import uuid

# Django
from django.db import models

def setting_directory_path(instance, filename):
    """ File will be uploaded to MEDIA_ROOT/site/logo/<filename> """

    ext = filename.split('.')[-1]
    name = uuid.uuid4()
    return f'site/logo/{name}.{ext}'

class Setting(models.Model):
    name = models.CharField(max_length=128)
    slogan = models.CharField(max_length=128)
    logo = models.ImageField(upload_to=setting_directory_path, null=True)
    email = models.EmailField(max_length=128)
    phone_number = models.CharField(max_length=15)
    intro_step = models.PositiveSmallIntegerField(default=1)
    description = models.CharField(max_length=240)
    keywords = models.CharField(max_length=240)

    def __str__(self):
        return self.name