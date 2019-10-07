from django.urls import path
from authentication import views as l_views
from authentication.views import (
    login,
    register,
    logout,
    reset
)

app_name = 'log'

urlpatterns = [

    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('reset/', reset, name='reset'),

]

