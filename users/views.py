
# Django
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse

# Models
from authentication.models import UserProfile

# Utils
from dashboard.utils import DataTable

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

def index(request):

    total_users = UserProfile.objects.all().count()

    context = {
        'total_users': total_users,
        'menu': 'users',
        }
    return render(request, 'users/index.html', context)

def create(request):
    pass

def read(request, id):
    pass

def update(request, id):
    pass

def delete(request, id):
    pass