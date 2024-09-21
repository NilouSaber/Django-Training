from django.shortcuts import render, get_object_or_404
from blog.models import post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
current_time = timezone.now()
def blog_view(request, **kwargs):
    
    posts = post.objects.filter(publishedDate__lte=current_time, status=1).order_by("-publishedDate")
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username =kwargs['author_username'])


#paginator
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    posts = posts.get_page(page_number)

    context = {"posts":posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    postd = post.objects.filter(publishedDate__lte=current_time, status=1).order_by("-publishedDate")
    posts = get_object_or_404(postd, pk=pid)
    posts.countedViews += 1
    posts.save()
    nxtPost = post.objects.filter(pk__gt=pid, status=1, publishedDate__lte=current_time).order_by('pk').first()
    prvPost = post.objects.filter(pk__lt=pid, status=1, publishedDate__lte=current_time).order_by('-pk').first()
    context = {'posts':posts, 'prvPost': prvPost, 'nxtPost': nxtPost}
    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    current_time = timezone.now()
    posts = post.objects.filter(publishedDate__lte=current_time, status=1).order_by("-publishedDate")
    if request.method == "GET":
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {"posts":posts}
    return render(request, 'blog/blog-home.html', context)