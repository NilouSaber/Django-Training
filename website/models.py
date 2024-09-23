from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=400)
    message = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ("createdDate", )
    def __str__(self):
        return self.subject
    
class newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email
    