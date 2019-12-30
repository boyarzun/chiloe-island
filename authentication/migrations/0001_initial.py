# Generated by Django 2.2.7 on 2019-12-30 01:11

import authentication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=18, null=True)),
                ('avatar', models.ImageField(default='avatar/default.png', upload_to=authentication.models.user_directory_path)),
                ('map', models.URLField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
