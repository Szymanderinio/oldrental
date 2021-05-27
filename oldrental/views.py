from django.shortcuts import render
from .models import Book


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the oldrental index.")


def books(request):
    books = Book.objects.filter().order_by('author')
    return render(request, 'books.html', {'books': books})
