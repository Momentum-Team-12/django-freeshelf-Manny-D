from django import forms
from .models import Book, Note, Image


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
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
        fields = ('title', 'image')