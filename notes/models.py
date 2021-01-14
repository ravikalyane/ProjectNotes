from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Note(models.Model):
    title = models.CharField(max_length=50)
    note = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    pinned = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)


class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, default=20)
    location = models.CharField(max_length=100, default='Mumbai')
    email = models.EmailField(default="someone@gmail.com")
    course = models.CharField(max_length=100, default='CS')
