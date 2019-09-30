from django.shortcuts import render


def index(request):
    context = { 'menu': 'users'}
    return render(request, 'users/index.html', context)

def create(request):
    pass

def read(request, id):
    pass

def update(request, id):
    pass

def delete(request, id):
    pass