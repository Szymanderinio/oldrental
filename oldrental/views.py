from django.shortcuts import render, redirect
from django.views import View

from .models import Book, RentedBook
from django.shortcuts import render, get_object_or_404
from .forms import BookForm

# Create your views here.
from django.http import HttpResponse


class BookRent(View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if request.user.is_authenticated:
            book.rent(request.user)
            book.save()
            return render(request, 'book_detail.html', {'book': book})
        else:
            return redirect('home')


class BookUnRent(View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.unrent()
        book.save()
        return render(request, 'book_detail.html', {'book': book})


class BookView(View):
    def get(self, request):
        books = Book.objects.filter().order_by('author')
        return render(request, 'books.html', {'books': books})


class BookEdit(View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book_temp = form.save(commit=False)
            book_temp.save()
            return render(request, 'book_detail.html', {'book': book_temp})

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, 'book_edit.html', {'book': form})


class BookNew(View):
    def post(self, request):
        book = BookForm(request.POST)
        if book.is_valid():
            book_temp = book.save(commit=False)
            book_temp.save()
            return render(request, 'book_detail.html', {'book': book_temp})

    def get(self, request):
        book = BookForm()
        return render(request, 'book_edit.html', {'book': book})


class BookDetail(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'book_detail.html', {'book': book})


class BookRemove(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('books')


class RentedBookView(View):
    def get(self, request):
        rentedbooks = RentedBook.objects.filter().order_by('date_to')
        return render(request, 'rentedbooks.html', {'rentedbooks': rentedbooks})


        # if request.user.is_authenticated:
        #     book.rent(request.user)
        #     book.save()
        #     return render(request, 'book_detail.html', {'book': book})
        # else:
        #     return redirect('home')