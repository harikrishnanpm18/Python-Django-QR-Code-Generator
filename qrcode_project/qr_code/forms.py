# qr_code_app/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
 
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
 
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
 
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)