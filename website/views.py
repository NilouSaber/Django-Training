from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import contactForm, newsletterForm
from django.contrib import messages
from blog.models import post
from django.utils import timezone
from .decorators import under_construction_only

current_time = timezone.now()
def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')

    
def contact_view(request):
    if request.method == "POST":
        form = contactForm(request.POST)     
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, "your ticket submitted successfully")
        else:
            messages.add_message(request,messages.ERROR, "your ticket didn't submitted")
    form = contactForm()
    return render(request, 'website/contacts.html', {'form' : form})

def newsletter_view(request):
    if request.method == "POST":
        form = newsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

# to disable it, just put UNDER_CONSTRUCTION = False in the settings.py
@under_construction_only
def under_construction(request):
    return render(request, 'under_construction.html')