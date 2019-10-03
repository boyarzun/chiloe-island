
import json
# Django
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

# Models
from authentication.models import UserProfile

# Forms
from authentication.forms import UserForm, UserProfileForm

# Utils
from dashboard.utils import DataTable, FormToJsonResponse

@login_required
def get_users_list(request):
    """ API for load data in DataTable """
    
    dt = DataTable(request)    
    users_list = UserProfile.objects.filter(user__first_name__contains = dt.search) | UserProfile.objects.filter(user__last_name__contains = dt.search)

    # Pagination
    paginator = Paginator(list(users_list), 15)
    users = paginator.get_page(dt.start)

    # Prepare data
    def sort_data(user_profile):
        return [
            user_profile.user.username,
            user_profile.user.first_name + ' ' + user_profile.user.last_name,
            user_profile.user.email,
            user_profile.address,
            user_profile.phone
        ]

    data_users = list(map(sort_data, users.object_list))

    data = {
        "draw": dt.draw,
        "recordsTotal": paginator.count,
        "recordsFiltered": paginator.count,
        "data": data_users
    }

    return JsonResponse(data, safe=False)

@login_required
def index(request):

    total_users = UserProfile.objects.all().count()

    if request.method == 'POST':

        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        form = FormToJsonResponse(user_profile_form, user_form)

        if form.is_valid():
            pass

        return JsonResponse(form.response)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {
        'total_users': total_users,
        'menu': 'users',
        'profile_form': profile_form,
        'user_form': user_form,
        }
    return render(request, 'users/index.html', context)

@login_required
def create(request):
    pass

@login_required
def read(request, id):
    pass

@login_required
def update(request, id):
    pass

@login_required
def delete(request, id):
    pass