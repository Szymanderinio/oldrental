from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from collections import Counter


class CDGenre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    @staticmethod
    def get_all_genres():
        return CDGenre.objects.all()

    def __str__(self):
        return self.name


class CD(models.Model):
    band = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    genre = models.ForeignKey(CDGenre, related_name='cds', on_delete=models.PROTECT)
    time = models.TimeField()
    usercd_rentier = models.ForeignKey(User, related_name='cds', on_delete=models.CASCADE,
                                       default=None, blank=True, null=True)
    rent_date = models.DateTimeField(default=None, blank=True, null=True)

    def rent(self, user):
        self.usercd_rentier = user
        self.rent_date = datetime.now()

    def unrent(self):
        RentedCD.objects.create(cd=self, user=self.usercd_rentier, date_from=self.rent_date)
        self.usercd_rentier = None
        self.rent_date = None

    class Meta:
        ordering = ('title',)


class Song(models.Model):
    title = models.CharField(max_length=64)
    cd = models.ForeignKey(CD, related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RentedCD(models.Model):
    cd = models.ForeignKey(CD, related_name='old_cd_rents', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateTimeField(datetime)
    date_to = models.DateTimeField(default=datetime.now())
