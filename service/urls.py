from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('home/', views.home, name='index'),
    path('about/',views.about, name='about'),
    path('price/',views.price, name='price'),
    path('result/',views.result, name='result'),

]