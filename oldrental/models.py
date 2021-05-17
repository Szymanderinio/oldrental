from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.PROTECT)
    isbn = models.CharField(unique=True, max_length=13, validators=[
        RegexValidator(regex='^[0-9]{13}$', message='ISBN must be 13 digit long!', code='no_match')])
    user_rentier = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE,
                                     default=None, blank=True, null=True)
    rent_date = models.DateTimeField(default=None, blank=True, null=True)

    def rent(self, user):
        self.user_rentier = user
        self.rent_date = datetime.now()

    def unrent(self):
        pass

    def get_absolute_url(self):
        return reverse('books:details', args=[self.pk])

    class Meta:
        unique_together = ('author', 'title', 'genre')
        ordering = ('title',)
