from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Note, Category
from .forms import BookForm
from .forms import NoteForm
from .forms import ImageForm
from .forms import Favorite
from .forms import FavoriteForm

def home(request):
	if request.user.is_authenticated:
		return redirect('list_books')
	return render(request, "base.html")

def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})

def book_detail(request,pk):
    form = FavoriteForm()
    book = Book.objects.get(pk=pk)
    context = {
        'book':book,
        'form':form,
    }
    return render(request, 'books/book_detail.html', context)    

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

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

def category_book(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)
    return render(request, "books/category.html", {'books':books, 'category':category})

def add_favorite(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        user = request.user
        form = FavoriteForm(data=request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.book = book
            favorite.user = user 
            favorite.save()
            return redirect(to='book_detail', pk=pk)

def favorite_book(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'books/favorite_book.html', {'favorites': favorites})