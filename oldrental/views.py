from django.shortcuts import render
from .models import Book
from django.shortcuts import render, get_object_or_404


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
