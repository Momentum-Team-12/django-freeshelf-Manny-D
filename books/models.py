from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse


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
    image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    # one to many relationship - book has one category but category has many books
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, related_name='books')

    def __str__(self):
	    return self.title

class Note(models.Model):
    album = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="notes")
    created_on = models.DateTimeField(auto_now_add=True)
    note = models.TextField(max_length=500)
    
    def __str__(self):
	    return self.title

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs=
        {'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE,related_name='favorites')
    user = models.ForeignKey('User', on_delete=models.CASCADE,related_name ='favorites')
    
