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

    # Social networks
    instagram = models.CharField(max_length=128, blank=True)
    twitter = models.CharField(max_length=128, blank=True)
    facebook = models.CharField(max_length=128, blank=True)

    # Template settings

    ## Menu options
    menu_color = models.PositiveSmallIntegerField()
    menu_dark = models.BooleanField()
    menu_collapsed = models.BooleanField()
    menu_selection = models.PositiveSmallIntegerField()

    ## Navbar options
    navbar_color = models.PositiveSmallIntegerField()
    navbar_dark = models.BooleanField()
    navbar_fixed = models.BooleanField()

    ## Footer options
    footer_dark = models.BooleanField()
    footer_fixed = models.BooleanField()


    def __str__(self):
        return self.name