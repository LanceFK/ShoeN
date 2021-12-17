from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date 
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    shoe_image = models.ImageField(null=False, blank=False, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Select Shoe')
    shoe_in = models.CharField(max_length=255)
    colaboration = models.CharField(max_length=255)
    color_scheme_1 = models.CharField(max_length=255)
    color_scheme_2 = models.CharField(max_length=255)
    color_scheme_3 = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name= 'blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
