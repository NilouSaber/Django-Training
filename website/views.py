from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>This is index<h1>')


def about_view(request):
    return HttpResponse('<h1>This is about<h1>')

    
def contact_view(request):
    return HttpResponse('<h1>This is contact<h1>')

