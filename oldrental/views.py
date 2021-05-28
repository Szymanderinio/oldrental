from django.shortcuts import render, redirect
from .models import Book
from django.shortcuts import render, get_object_or_404
from .forms import BookForm

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the oldrental index.")


def books(request):
    books = Book.objects.filter().order_by('author')
    return render(request, 'books.html', {'books': books})


def books_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def book_new(request):
    if request.method == "POST":
        book = BookForm(request.POST)
        if book.is_valid():
            book_temp = book.save(commit=False)
            book_temp.save()
            return redirect('book_detail.html', pk=book_temp.pk)
    else:
        book = BookForm()
    return render(request, 'book_edit.html', {'book': book})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book_temp = form.save(commit=False)
            book_temp.save()
            return redirect('book_detail.html', pk=book_temp.pk)
    else:
        book = BookForm(instance=book)
    return render(request, 'book_edit.html', {'book': book})
