from django.contrib import admin
from website.models import contact
# Register your models here.

class contactAdmin(admin.ModelAdmin):
    date_hierarchy = "createdDate"
    list_display = ("name", "email", "subject",)
    list_filter = ("email", )
    search_fields = ("name", "family", "subject", "content",)
admin.site.register(contact, contactAdmin)