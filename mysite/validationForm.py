from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from captcha.fields import CaptchaField


User = get_user_model()
# password reset form
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise ValidationError("This email address is not registered.")
        return email

class CustomPasswordResetView(auth_views.PasswordResetView):
    form_class = CustomPasswordResetForm

# conformation and set password
class CustomPasswordResetConfirmForm(SetPasswordForm):
    captcha = CaptchaField()

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm