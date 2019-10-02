from django.urls import path
from users.views import index, get_users_list

app_name = 'users'

urlpatterns = [
    path('users', index, name='index'),
    path('users/list', get_users_list, name='datatable')
]

