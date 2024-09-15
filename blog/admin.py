from django.contrib import admin
from blog.models import post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "createdDate"
    empty_value_display = "-empty-"
    list_display = ("title", "createdDate", "countedViews", "status", "publishedDate", )
    list_filter = ("status", )
#    ordering = ("createdDate", )
    search_fields = ("title", "content", )
admin.site.register(post, PostAdmin)