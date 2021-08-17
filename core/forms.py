from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Profil,Photo
from django.forms import inlineformset_factory



class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter Username"
    }))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Enter Email"
    }))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter Password"
    }))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter Password"
    }))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProfilForm(forms.ModelForm):
    class Meta:
        model=Profil
        exclude=()

