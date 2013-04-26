from django.db import models
from django.utils.translation import gettext as _
from base import LocationBase

__all__ = ['Subregion']

class Subregion(LocationBase):
    region = models.ForeignKey('Region', related_name='%(app_label)s_%(class)s_region', null=True, blank=True)
    capital = models.ForeignKey('City', related_name='%(app_label)s_%(class)s_capital', null=True, blank=True)
    code = models.CharField(_('Code'), max_length=40, null=True, blank=True)
    fips = models.CharField(_('FIPS code'), max_length=40, blank=True, null=True)

    class Meta:
        app_label = 'geoware'
        db_table = app_label + '-subregion'
        unique_together = [('name', 'region')]

    @property
    def parent(self):
        return self.region


