from django import forms

from dal import autocomplete

from ..models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(url='geoware:country-autocomplete'),
            'division': autocomplete.ModelSelect2(url='geoware:division-autocomplete'),
            'subdivision': autocomplete.ModelSelect2(url='geoware:subdivision-autocomplete'),
            'district_of': autocomplete.ModelSelect2(url='geoware:city-autocomplete'),
        }
