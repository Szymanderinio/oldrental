from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:pk>/rent/', views.rentMe, name='book_rent'),
    path('<int:pk>/unrent/', views.unRentMe, name='book_unrent'),
    path('<int:pk>/', views.books_detail, name='books_detail'),
    path('new', views.book_new, name='book_new'),
    path('<int:pk>/edit/', views.book_edit, name='book_edit'),

]
