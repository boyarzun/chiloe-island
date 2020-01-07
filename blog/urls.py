from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # Public store
    path('blog', index, name="index"),
]

