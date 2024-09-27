from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['postc','name', 'subject', 'email', 'message']
