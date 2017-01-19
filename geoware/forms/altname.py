from django import forms
from django.utils.translation import ugettext as _

from dal.autocomplete import ModelSelect2

from ..models import Altname


class AltnameForm(forms.ModelForm):
    """
    Custom Altname Form.
    """
    class Meta:
        model = Altname
        fields = ('__all__')
        widgets = {
            'language': ModelSelect2(
                url='geoware:language-autocomplete',
                attrs={
                    'data-placeholder': _('LOCATION.DIVISION'),
                    'data-minimum-input-length': 0,
                }
            ),
        }
