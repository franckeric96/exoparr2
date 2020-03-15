from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('singleblog', views.singleblog, name='singleblog'),
    path('rooms', views.rooms, name='rooms'),
    path('elements', views.elements, name='elements') 


     
]