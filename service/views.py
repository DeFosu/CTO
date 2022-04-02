from email import message
from urllib import request
from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.db.models import Q

def home(request):
    posts = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'service/home.html', {'posts': posts})

def about(request):
    return render(request, 'service/about.html')

def price(request):
    services = Service.objects.all
    return render(request, 'service/price.html', {'services':services})

def result(request):
    if (request.GET.get('q')):
        query = request.GET.get('q')
        tmp_list = Service.objects.filter(Q(cost__icontains = query)) 
    return render(request, 'service/result.html', {'tmp': tmp_list})


    