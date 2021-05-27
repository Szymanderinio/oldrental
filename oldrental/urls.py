from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('book/<int:pk>/', views.books_detail, name='books_detail'),

]
