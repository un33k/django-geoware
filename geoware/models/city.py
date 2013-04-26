from django.db import models
from django.utils.translation import gettext as _
from base import CityBase

__all__ = ['City']

class City(CityBase):

    country = models.ForeignKey('Country', related_name='%(app_label)s_%(class)s_country', null=True, blank=True)
    region = models.ForeignKey('Region', related_name='%(app_label)s_%(class)s_region', blank=True, null=True)
    subregion = models.ForeignKey('Subregion', related_name='%(app_label)s_%(class)s_subregion', blank=True, null=True)
    timezone = models.ForeignKey('Timezone', related_name='%(app_label)s_%(class)s_timezone', blank=True, null=True)
    sister = models.ForeignKey('City', help_text=_('Sister Cities'), blank=True, null=True)

    class Meta:
        app_label = 'geoware'
        db_table = app_label + '-city'
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        # unique_together = (('name', 'region'),)

    @property
    def parent(self):
        if self.subregion and self.subregion.parent:
            return self.subregion
        else:
            return self.region



