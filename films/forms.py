from django import forms

from .models import Film


class FilmNewForm(forms.ModelForm):
    class Meta:
        model = Film
        exclude = ('userfilm_rentier', 'rent_date')
