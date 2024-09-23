from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import contactForm, newsletterForm
from django.contrib import messages

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
    
