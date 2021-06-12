from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class FilmGenre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    @staticmethod
    def get_all_genres():
        return FilmGenre.objects.all()

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=64)
    director = models.CharField(max_length=64)
    genre = models.ForeignKey(FilmGenre, related_name='films', on_delete=models.PROTECT)
    time = models.TimeField()
    userfilm_rentier = models.ForeignKey(User, related_name='films', on_delete=models.CASCADE,
                                       default=None, blank=True, null=True)
    rent_date = models.DateTimeField(default=None, blank=True, null=True)

    def rent(self, user):
        self.userfilm_rentier = user
        self.rent_date = datetime.now()

    def unrent(self):
        RentedFilm.objects.create(film=self, user=self.userfilm_rentier, date_from=self.rent_date)
        self.userfilm_rentier = None
        self.rent_date = None

    class Meta:
        unique_together = ('title', 'director', 'time')
        ordering = ('title',)


class RentedFilm(models.Model):
    film = models.ForeignKey(Film, related_name='old_film_rents', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateTimeField(datetime)
    date_to = models.DateTimeField(default=datetime.now())
