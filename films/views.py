from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import Film, RentedFilm
from .forms import FilmNewForm


# Create your views here.

class FilmView(View):
    def get(self, request):
        films = Film.objects.filter().order_by('title')
        return render(request, 'films.html', {'films': films})


class FilmNew(View):
    def post(self, request):
        film = FilmNewForm(request.POST)
        if film.is_valid():
            film_temp = film.save(commit=False)
            film_temp.save()
            return render(request, 'film_detail.html', {'film': film_temp})

    def get(self, request):
        film = FilmNewForm()
        return render(request, 'film_edit.html', {'film': film})


class FilmDetail(View):
    def get(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        return render(request, 'film_detail.html', {'film': film})


class FilmEdit(View):
    def post(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        form = FilmNewForm(request.POST, instance=film)
        if form.is_valid():
            film_temp = form.save(commit=False)
            film_temp.save()
            return render(request, 'film_detail.html', {'film': film_temp})

    def get(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        form = FilmNewForm(instance=film)
        return render(request, 'film_edit.html', {'film': form})


class FilmRemove(View):
    def get(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        film.delete()
        return redirect('films')


class RentedFilmView(View):
    def get(self, request):
        rentedfilms = RentedFilm.objects.filter().order_by('-date_to')
        return render(request, 'rentedfilms.html', {'rentedfilms': rentedfilms})


class FilmRent(View):
    def post(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        if request.user.is_authenticated:
            film.rent(request.user)
            film.save()
            return render(request, 'film_detail.html', {'film': film})
        else:
            return redirect('home')


class FilmUnRent(View):
    def post(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        film.unrent()
        film.save()
        return render(request, 'film_detail.html', {'film': film})
