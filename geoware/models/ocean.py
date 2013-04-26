from django.db import models
from base import LocationBase
from django.utils.translation import gettext as _


__all__ = ['Ocean']

class Ocean(LocationBase):

    depth = models.PositiveIntegerField(_('Greatest Depth'), null=True, blank=True)
    depth_name = models.CharField(_('Depth Name'), max_length=254, null=True, blank=True)

    class Meta:
        app_label = 'geoware'
        db_table = app_label + '-ocean'

    @property
    def parent(self):
        return None


