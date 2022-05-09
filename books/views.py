from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .models import Note
from .forms import BookForm
from .forms import NoteForm


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})


def new_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(request, "books/new_book.html", {"form": form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(request, "books/edit_book.html", {
        "form": form,
        "book": book
    })


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='list_books')

    return render(request, "books/delete_book.html", {"book": book})


def notes_book(request, pk): 
    book = get_object_or_404(Book, pk=pk)

    return render(request, "books/notes_book.html", {"book": book})

def add_note(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.book = book
            new_note.save()
            return redirect(to='notes_book' ,pk=pk)

    return render(request, "books/add_note.html", {
        "form": form,
        "book": book
    })