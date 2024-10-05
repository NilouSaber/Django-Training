from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'UNDER_CONSTRUCTION', False):
            # Allow access to the admin site and the under construction page
            if request.path.startswith('/admin/') or request.path == reverse('website:under_construction'):
                return self.get_response(request)

            # Allow access to captcha URLs
            if 'captcha' in request.path:
                return self.get_response(request)

            # Redirect all other requests to the under construction view
            return redirect(reverse('website:under_construction'))

        return self.get_response(request)