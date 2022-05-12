from django import forms
from .models import Book, Favorite, Note, Image


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            # 'image',
            'url',
        ]

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'note',
        ]

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = [
            'title', 
            'image',
        ]

class FavoriteForm(forms.ModelForm):
        class Meta:
            model = Favorite
            fields = [
        ]