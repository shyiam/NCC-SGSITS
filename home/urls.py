from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about', views.about, name='About'),
    path('cc', views.cc, name='Cadets Corner'),
    path('alumni', views.alumni, name='Alumni'),
    path('downloads', views.downloads, name='Downloads'),
    path('contact', views.contact, name='Contact'),

]
