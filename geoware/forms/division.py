from django import forms
from django.utils.translation import ugettext as _

from dal import autocomplete
from dal import forward

from ..models import Division


class DivisionForm(forms.ModelForm):
    """
    Custom Division Form.
    """
    class Meta:
        model = Division
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2(
                url='geoware:country-autocomplete',
                attrs={
                    'data-placeholder': _('LOCATION.COUNTRY'),
                    'data-minimum-input-length': 0,
                }
            ),
            'capital': autocomplete.ModelSelect2(
                url='geoware:city-autocomplete',
                forward=['country', ],
                attrs={
                    'data-placeholder': _('LOCATION.CAPITAL'),
                    'data-minimum-input-length': 0,
                }
            ),
        }
