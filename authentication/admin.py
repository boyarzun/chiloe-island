from django.contrib import admin
from authentication.models import UserProfile, Commune

admin.site.register(UserProfile)
admin.site.register(Commune)
