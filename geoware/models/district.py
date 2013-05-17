from django.db import models
from django.utils.translation import gettext as _
from base import CityBase

__all__ = ['District']

class District(CityBase):
    city = models.ForeignKey('City', related_name='%(app_label)s_%(class)s_city', null=True, blank=True)

    class Meta:
        app_label = 'geoware'
        db_table = app_label + '-district'
        unique_together = [('name', 'city')]

    @property
    def parent(self):
        if self.city:
            return self.city
        return None


