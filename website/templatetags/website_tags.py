from django import template
from blog.models import post, Category
from django.utils.timezone import now
register = template.Library()

current_time = now()
@register.inclusion_tag('website/recent.html')
def recentposts(arg=6):
    posts = post.objects.filter(publishedDate__lte=current_time,status=1).order_by('-publishedDate')[:arg]
    return {"posts":posts}