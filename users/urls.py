from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.auth_login, name='auth_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
