from django import forms
from django.utils.translation import ugettext as _

from dal import autocomplete
from dal import forward

from ..models import Ocean


class OceanForm(forms.ModelForm):
    """
    Custom Ocean Form.
    """
    class Meta:
        model = Ocean
        fields = (
            'name',
            'name_std',
            'area',
            'is_active',
            'depth',
            'depth_name',
            'altnames',
            'url',
            'info',
        )
