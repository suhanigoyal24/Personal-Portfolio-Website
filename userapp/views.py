
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile, Skill, Experience

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        full_name = request.POST['full_name']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        Profile.objects.create(user=user, full_name=full_name)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard_view(request):
    profile = Profile.objects.get(user=request.user)
    skills = Skill.objects.filter(profile=profile)
    experiences = Experience.objects.filter(profile=profile)
    return render(request, 'dashboard.html', {'profile': profile, 'skills': skills, 'experiences': experiences})

