from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SignUpForm(instance=user)
    return render(request, 'dashboard.html', {'form': form})
