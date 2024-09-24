from django import forms
from website.models import contact, newsletter

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"
    def save(self, commit=True):
        preSave = super(contactForm, self).save(commit=False)
        preSave.name = "Unknown"

        if commit:
            preSave.save()
        return preSave

class newsletterForm(forms.ModelForm):
    class Meta:
        model = newsletter  
        fields = "__all__"
