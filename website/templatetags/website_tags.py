from django import template
from blog.models import post, Category

register = template.Library()

@register.inclusion_tag('website/recent.html')
def recentposts(arg=6):
    posts = post.objects.filter(status=1).order_by('-publishedDate')[:arg]
    return {"posts":posts}