from django.urls import path
from website.views import index_view, contact_view, about_view, newsletter_view

app_name = 'website'
urlpatterns = [
    path('', index_view, name="index"),
    path('about', about_view, name="about"),
    path('contacts', contact_view, name="contacts"),
    path('newsletter', newsletter_view, name="newsletter")
]
