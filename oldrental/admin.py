from django.contrib import admin
from .models import Genre, Book, RentedBook
from cds.models import CD, CDGenre, Song, RentedCD
from films.models import Film, FilmGenre, RentedFilm

# Register your models here.
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(RentedBook)

admin.site.register(CD)
admin.site.register(CDGenre)
admin.site.register(Song)
admin.site.register(RentedCD)

admin.site.register(Film)
admin.site.register(FilmGenre)
admin.site.register(RentedFilm)
