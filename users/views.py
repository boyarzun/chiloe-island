
import json
# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse

# Models
from authentication.models import UserProfile
from django.contrib.auth.models import User

# Forms
from authentication.forms import UserForm, UserProfileForm

# Utils
from core.utils import DataTable

@login_required
def get_users_list(request):
    """ API for load data in DataTable """

    active_users = request.GET.get('active')
    dt = DataTable(request)

    if active_users == "true":
        users_list = UserProfile.objects.filter(user__is_active = True)
    elif active_users == "false":
        users_list = UserProfile.objects.filter(user__is_active = False)
    else:
        users_list = UserProfile.objects.filter(user__first_name__contains = dt.search) | UserProfile.objects.filter(user__last_name__contains = dt.search)



    # Pagination
    paginator = Paginator(list(users_list), 15)
    users = paginator.get_page(dt.start)
    # Prepare data
    def sort_data(profile):
        return [
            profile.user.first_name + ' ' + profile.user.last_name,
            profile.user.email,
            '<a href="/users/' + str(profile.user.pk)  + '/edit"><i class="material-icons">edit</i></a>\
            <a href="#" ><i onclick="remove(event);return false;" data-user-id="' + str(profile.user.pk) + '" class="material-icons">delete</i></a>'
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

    context = {
        'total_users': total_users,
        'menu': 'users',
        }
    return render(request, 'users/index.html', context)

@login_required
def create(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, 'Usuario creado!')
            return redirect(reverse('users:index'))

    else:
        user_form = UserForm()

    context = {
        'user_form': user_form,
        'menu': 'users',
    }

    return render(request, 'users/create.html', context)

@login_required
def update(request, id):
    user = get_object_or_404(User, pk=id)
    user_form = UserForm(request.POST or None, instance=user)
    profile_form = UserProfileForm(request.POST or None, request.FILES, instance=user.userprofile)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(request, 'Usuario actualizado!')

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'menu': 'users'
    }
    return render(request, 'users/update.html', context)

@login_required
def delete(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    data = {
        'ok': True
    }
    return JsonResponse(data)