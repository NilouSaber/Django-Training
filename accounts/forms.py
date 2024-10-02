from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from captcha.fields import CaptchaField

UserModel = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')

class CustomAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'password', 'captcha')