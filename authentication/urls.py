from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from authentication import views as l_views
from authentication.views import (
    login,
    register,
    logout,
    AuthenticationPasswordResetView
)

app_name = 'log'

urlpatterns = [
    path('password_reset/', AuthenticationPasswordResetView.as_view(extra_context = {'compa': 'compa'}), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(extra_context = {'compa': 'compa'}), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(extra_context = {'compa': 'compa'}, success_url = reverse_lazy('authentication:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(extra_context = {'compa': 'compa'}), name='password_reset_complete'),

    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]

