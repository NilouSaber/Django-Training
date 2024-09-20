from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    # tags = 
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    countedViews = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)
    publishedDate = models.DateTimeField(null=True)
    class Meta:
        ordering = ["-createdDate",]
        verbose_name = "blog post"
    def __str__(self):
        return self.title


    
    