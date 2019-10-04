from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length = 30, null=True)
    phone = models.CharField(max_length=18, null=True)

    def __str__(self):
        return "Usuario: %s" % (self.user)
