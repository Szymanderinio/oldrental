from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('book/<int:pk>/', views.books_detail, name='books_detail'),
    path('book/new', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),

]
