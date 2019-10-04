from django.urls import path
from users.views import index, get_users_list, create, delete, update

app_name = 'users'

urlpatterns = [
    path('users', index, name='index'),
    path('users/list', get_users_list, name='datatable'),
    path('users/new', create, name='create'),
    path('users/<int:id>/delete', delete, name='delete'),
    path('users/<int:id>/edit', update, name='edit'),
]

