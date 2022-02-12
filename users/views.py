from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def signin(request):
    return render(request, 'users/signin.html')


def signup(request):
    return render(request, 'users/signup.html')


def register(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username,
                                        email=email, password=password)

        messages.success(request, "Registered successfully. Please Login")
        return redirect('signin')
    else:
        messages.warning(request, "Error occurred. Please Try Again")
        return redirect('signup')


def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.POST.get('next'):
                return redirect(request.POST.get('next'))
            else:
                messages.success(request, "Logged In Successfully")
                return redirect('home')

        else:
            messages.warning(request, "Invalid Credentials. Please Try Again")
            return redirect('signin')


def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')
