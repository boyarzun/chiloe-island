from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True, default=None, on_delete=models.CASCADE)
    address = models.CharField(max_length = 30)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return "Usuario: %s" % (self.user)
