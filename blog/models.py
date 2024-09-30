from django.db import models
import datetime
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    countedViews = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)
    publishedDate = models.DateTimeField(null=True)
    login_require = models.BooleanField(default=False)
    class Meta:
        ordering = ["-createdDate",]
        verbose_name = "blog post"
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})
    

class Comment(models.Model):
    postc = models.ForeignKey(post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-createdDate",]
    def __str__(self):
        return self.name
    
    