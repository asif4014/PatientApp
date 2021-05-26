from django.contrib import admin
from django.urls import path, include
from patientapp import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('add/register',views.register, name = 'register'),
    path('fetch/auth_user',views.auth_user, name = 'auth_user'),
    path('add/',views.addUserInfo, name = 'addUser'),
    path('fetch/',views.fetchUserInfo, name = 'fetch'),


]