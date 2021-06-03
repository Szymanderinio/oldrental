from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


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
        RentedBook.objects.create(book=self, user=self.user_rentier, date_from=self.rent_date)
        self.user_rentier = None
        self.rent_date = None

    class Meta:
        unique_together = ('author', 'title', 'genre')
        ordering = ('title',)


class RentedBook(models.Model):
    book = models.ForeignKey(Book, related_name='old_rents', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateTimeField(datetime)
    date_to = models.DateTimeField(default=datetime.now())











