from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookView.as_view(), name='books'),
    path('<int:pk>/rent/', views.BookRent.as_view(), name='book_rent'),
    path('<int:pk>/unrent/', views.BookUnRent.as_view(), name='book_unrent'),
    path('detail/<int:pk>/', views.BookDetail.as_view(), name='books_detail'),
    path('new', views.BookNew.as_view(), name='book_new'),
    path('<int:pk>/edit/', views.BookEdit.as_view(), name='book_edit'),
    path('remove/<int:pk>', views.BookRemove.as_view(), name='book_remove')

]
