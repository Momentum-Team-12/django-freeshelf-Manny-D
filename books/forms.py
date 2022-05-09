from django import forms
from .models import Book, Note


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