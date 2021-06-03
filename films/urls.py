from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmView.as_view(), name='films'),
    path('<int:pk>/rent/', views.FilmRent.as_view(), name='film_rent'),
    path('<int:pk>/unrent/', views.FilmUnRent.as_view(), name='film_unrent'),
    path('detail/<int:pk>/', views.FilmDetail.as_view(), name='film_detail'),
    path('new', views.FilmNew.as_view(), name='film_new'),
    path('<int:pk>/edit/', views.FilmEdit.as_view(), name='film_edit'),
    path('remove/<int:pk>', views.FilmRemove.as_view(), name='film_remove'),
    path('rentedfilms/', views.RentedFilmView.as_view(), name='rentedfilms')
]
