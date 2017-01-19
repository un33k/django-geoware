from django import forms
from django.utils.translation import ugettext as _

from dal import autocomplete

from ..models import City


class CityForm(forms.ModelForm):
    """
    Custom City Form.
    """
    class Meta:
        model = City
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(
                url='geoware:country-autocomplete',
                attrs={
                    'data-placeholder': _('LOCATION.COUNTRY'),
                    'data-minimum-input-length': 0,
                }
            ),
            'division': autocomplete.ModelSelect2(
                url='geoware:division-autocomplete',
                forward=['country'],
                attrs={
                    'data-placeholder': _('LOCATION.DIVISION'),
                    'data-minimum-input-length': 0,
                }
            ),
            'subdivision': autocomplete.ModelSelect2(
                url='geoware:subdivision-autocomplete',
                forward=['division'],
                attrs={
                    'data-placeholder': _('LOCATION.SUBDIVISION'),
                    'data-minimum-input-length': 0,
                }
            ),
            'district_of': autocomplete.ModelSelect2(
                url='geoware:city-autocomplete',
                forward=['country', 'division', 'subdivision'],
                attrs={
                    'data-placeholder': _('LOCATION.CITY.DISTRICT_OF'),
                    'data-minimum-input-length': 0,
                }
            ),
            'timezone': autocomplete.ModelSelect2(
                url='geoware:timezone-autocomplete',
                forward=['country'],
                attrs={
                    'data-placeholder': _('LOCATION.TIMEZONE'),
                    'data-minimum-input-length': 0,
                }
            ),
            'altnames': autocomplete.ModelSelect2Multiple(
                url='geoware:altnames-autocomplete',
                forward=['geoname_id'],
                attrs={
                    'data-placeholder': _('LOCATION.ALTNAME'),
                },
            ),
        }
