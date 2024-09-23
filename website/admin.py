from django.contrib import admin
from website.models import contact, newsletter
# Register your models here.

class contactAdmin(admin.ModelAdmin):
    date_hierarchy = "createdDate"
    list_display = ("name", "email", "subject",)
    list_filter = ("email", )
    search_fields = ("name", "family", "subject", "content", 'createdDate')
admin.site.register(contact, contactAdmin)
admin.site.register(newsletter)