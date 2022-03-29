from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'service/home.html')

def about(request):
    return render(request, 'service/about.html')

def price(request):
    services = Service.objects.all
    return render(request, 'service/price.html', {'services':services})