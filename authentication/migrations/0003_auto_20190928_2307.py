# Generated by Django 2.2.5 on 2019-09-28 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_userprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
