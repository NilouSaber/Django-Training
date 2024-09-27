from django.contrib import admin
from blog.models import post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "createdDate"
    empty_value_display = "-empty-"
    list_display = ("title", "pk" , "author", "createdDate", "countedViews", "status", "publishedDate")
    list_filter = ("status", "author")
#    ordering = ("createdDate", )
    search_fields = ("title", "content", )
    summernote_fields = ('content',)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "createdDate"
    empty_value_display = "-empty-"
    list_display = ("name", "postc" , "approved", "createdDate")
    list_filter = ("postc", "approved")
    search_fields = ("name", "postc", )


admin.site.register(Comment, CommentAdmin)
admin.site.register(post, PostAdmin)
admin.site.register(Category)