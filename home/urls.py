from django.contrib import admin
from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html',views.index, name='index'),
    path('explore.html',views.explore, name='explore'),
    path('rooms.html',views.rooms, name='rooms'),
    path('bb.html',views.booking, name='booking'),
    path('contact.html',views.contact_view, name='contact'),
    path('new.html',views.newpage, name='my_bookings'),
    path('form', views.handle_form, name='handle_form'),
]