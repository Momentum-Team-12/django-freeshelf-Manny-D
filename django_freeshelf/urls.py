"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from django.urls import include
from books import views as books_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path("", books_views.home, name="home"),
    path('books/new/', books_views.new_book, name='new_book'),
    path('books/<int:pk>/edit/', books_views.edit_book,name='edit_book'),
    path('books/<int:pk>/delete/', books_views.delete_book, name='delete_book'),
    path('books/<int:pk>/', books_views.notes_book,name='notes_book'),
    path('books/<int:pk>/notes/', books_views.add_note, name='add_note'),
    path('upload/', books_views.image_upload_view),
    path('books/<slug:slug>/', books_views.category_book,name='category'),
    path('books/<slug:slug>/', books_views.category_book,name='favorite'),
    path('books/', books_views.list_books, name='list_books'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)