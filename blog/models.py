from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blogs(models.Model):
         title = models.CharField(max_length=255)
         subtitle = models.CharField(max_length=255, blank=True, null= True)
         description = models.TextField()
         image = models.FileField(upload_to='blog-post-image', blank=True, null= True)
         created_at = models.DateTimeField(auto_now_add=True)
         author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)