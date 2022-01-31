from django.db import models

# Create your models here.
class contacts(models.Model):
    Name = models.CharField( max_length=50)
    LastName = models.CharField( max_length=50)
    Age = models.IntegerField()
    Email = models.EmailField(max_length=50)
    Message = models.TextField(max_length=100)

class Post(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField(max_length = 100)