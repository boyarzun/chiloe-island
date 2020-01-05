# Generated by Django 2.2.7 on 2020-01-05 14:19

from django.db import migrations, models
import settings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slogan', models.CharField(max_length=128)),
                ('logo', models.ImageField(null=True, upload_to=settings.models.setting_directory_path)),
                ('email', models.EmailField(max_length=128)),
                ('phone_number', models.CharField(max_length=15)),
                ('intro_step', models.PositiveSmallIntegerField(default=1)),
                ('description', models.CharField(max_length=240)),
                ('keywords', models.CharField(max_length=240)),
                ('instagram', models.CharField(blank=True, max_length=128)),
                ('twitter', models.CharField(blank=True, max_length=128)),
                ('facebook', models.CharField(blank=True, max_length=128)),
                ('menu_color', models.PositiveSmallIntegerField()),
                ('menu_dark', models.BooleanField()),
                ('menu_collapsed', models.BooleanField()),
                ('menu_selection', models.PositiveSmallIntegerField()),
                ('navbar_color', models.PositiveSmallIntegerField()),
                ('navbar_dark', models.BooleanField()),
                ('navbar_fixed', models.BooleanField()),
                ('footer_dark', models.BooleanField()),
                ('footer_fixed', models.BooleanField()),
            ],
        ),
    ]
