from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="", default="blog_default.jpg")
    slug = models.SlugField(default='',null=False)

    
    def __str__(self):
        return f"{self.title}"
