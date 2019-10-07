from django.db import models

class Setting(models.Model):
    name = models.CharField(max_length=128)
    slogan = models.CharField(max_length=128)
    logo = models.ImageField(upload_to='site', null=True)
    intro_step = models.PositiveSmallIntegerField(default=1)
    description = models.CharField(max_length=240)
    keywords = models.CharField(max_length=240)

    def __str__(self):
        return self.name