from django import forms
from django.utils.translation import ugettext as _

from dal import autocomplete
from dal import forward

from ..models import Subdivision


class SubdivisionForm(forms.ModelForm):
    """
    Custom Subdivision Form.
    """
    class Meta:
        model = Subdivision
        fields = ('__all__')
        widgets = {
            'division': autocomplete.ModelSelect2(
                url='geoware:division-autocomplete',
                forward=['country'],
                attrs={
                    'data-placeholder': _('LOCATION.DIVISION'),
                    'data-minimum-input-length': 0,
                }
            ),
            'capital': autocomplete.ModelSelect2(
                url='geoware:city-autocomplete',
                forward=['division', ],
                attrs={
                    'data-placeholder': _('LOCATION.CAPITAL'),
                    'data-minimum-input-length': 0,
                }
            ),
        }
