from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'static/img/')
    url = models.URLField(max_length=200, null=True, blank=True)

class Note(models.Model):
    album = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="notes")
    created_on = models.DateTimeField(auto_now_add=True)
    note = models.TextField(max_length=500)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title