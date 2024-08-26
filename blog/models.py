from django.db import models

# Create your models here.
class post(models.Model):
    title = models.Charfield(max_length=255)
    content = models.Textfield()