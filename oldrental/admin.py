from django.contrib import admin
from .models import Genre, Book
from cds.models import CD, CDGenre, Song

# Register your models here.
admin.site.register(Genre)
admin.site.register(Book)

admin.site.register(CD)
admin.site.register(CDGenre)
admin.site.register(Song)
