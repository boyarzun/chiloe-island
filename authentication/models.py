# Django
from django.conf import settings

# Models
from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<user_id>/<filename>
    return 'users/{0}/{1}'.format(instance.user.id, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length = 30, null=True)
    phone = models.CharField(max_length=18, null=True)
    avatar = models.ImageField(upload_to=user_directory_path, default='avatar/default.png')

    def __str__(self):
        return "Usuario: %s" % (self.user)
