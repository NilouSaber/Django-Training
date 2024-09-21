from django.shortcuts import render, get_object_or_404
from blog.models import post
from django.utils import timezone

# Create your views here.
def blog_view(request, cat_name=None, author_username=None):
    current_time = timezone.now()
    posts = post.objects.filter(publishedDate__lte=current_time, status=1).order_by("-publishedDate")
    if cat_name:
        posts = posts.filter(category__name=cat_name)

    if author_username:
        posts = posts.filter(author__username = author_username)

    context = {"posts":posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = get_object_or_404(post, pk=pid, status=1)
    posts.countedViews += 1
    posts.save()
    nxtPost = post.objects.filter(pk__gt=pid, status=1).order_by('pk').first()
    prvPost = post.objects.filter(pk__lt=pid, status=1).order_by('-pk').first()
    context = {'posts':posts, 'prvPost': prvPost, 'nxtPost': nxtPost}
    return render(request, 'blog/blog-single.html', context)


