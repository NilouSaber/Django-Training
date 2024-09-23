from django import template
from blog.models import post
from blog.models import Category
register = template.Library()
@register.simple_tag(name='posts')
def function():
    posts=post.objects.filter(status=1)
    return posts

@register.inclusion_tag('blog/blog-latestposts.html')
def latestposts(arg=4):
    posts = post.objects.filter(status=1).order_by('publishedDate')[:arg] 
    return {"posts":posts}
    
@register.inclusion_tag("blog/blog-category.html")
def postcategories():
    posts = post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()

    return {"categories":cat_dict}
