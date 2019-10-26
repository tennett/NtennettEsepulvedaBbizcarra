from django.shortcuts import render
from .models import pelicula, user

def index (request):
# Create your views here.
    num_users = user.objects.all().count()
    return render(request, 'index.html', context={'num_books':num_users})