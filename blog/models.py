from django.db import models
import datetime
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    #thumbImage = models.ImageField(upload_to='blog_thumb/', default="blog_thumb/default.jpg")
    #thumbImage = models.ImageField(upload_to='blog_thumb', height_field='60', width_field='60', max_length=100, default="blog_thumb/default.jpg")
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
       
def resize_image(self):
        img = Image.open(self.image.path)
        if img.height > 60 or img.width > 60:
            output_size = (60, 60)
            img.thumbnail(output_size)
            img.save('blog_thumb')

    
    