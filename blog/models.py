from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # image =
    # tags = 
    # category = 
    # author = 
    countedViews = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)
    publishedDate = models.DateTimeField(null=True)
