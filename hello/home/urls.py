from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('newvehicles', views.newvehicles, name='newvehicles'),
    path('repair', views.repair, name='repair'),
    path('usedvehicles', views.usedvehicles, name='usedvehicles'),
] 
