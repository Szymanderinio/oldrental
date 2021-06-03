from django import forms

from .models import CD


class CDNewForm(forms.ModelForm):
    class Meta:
        model = CD
        exclude = ('usercd_rentier', 'rent_date')
