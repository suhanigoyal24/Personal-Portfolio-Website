from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile

# 🔹 Get the correct user model (CustomUser)
User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # 🔹 Use CustomUser instead of default User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'bio', 'skills', 'experience', 'resume', 'profile_img')
