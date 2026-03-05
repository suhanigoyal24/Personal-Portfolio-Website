from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm
from .models import UserProfile

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        pform = ProfileForm(request.POST, request.FILES, instance=profile)
        if pform.is_valid():
            pform.save()
            return redirect('dashboard')
    else:
        pform = ProfileForm(instance=profile)
    return render(request, 'dashboard.html', {'pform': pform})

# Add this at the end
@login_required
def preview(request):
    profile = request.user.userprofile
    return render(request, 'preview.html', {'profile': profile})
