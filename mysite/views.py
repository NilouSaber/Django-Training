from django.http import HttpResponse

def http_test(request):
    return HttpResponse('<h1>This is a test<h1>')
