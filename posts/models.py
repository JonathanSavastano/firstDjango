from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField() # relates to a text area form input
    slug = models.SlugField() 
    date = models.DateTimeField(auto_now_add=True) # date timestamp anytime post is added
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    # return the title when we query the database in ORM
    def __str__(self):
        return self.title 