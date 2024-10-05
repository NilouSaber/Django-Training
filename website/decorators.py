from django.conf import settings
from django.http import HttpResponseForbidden

def under_construction_only(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not getattr(settings, 'UNDER_CONSTRUCTION', False):
            return HttpResponseForbidden("This page is not available.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func