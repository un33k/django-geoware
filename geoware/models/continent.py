
from django.db import models
from django.utils.translation import gettext as _
from base import LocationBase


__all__ = ['Continent']

class Continent(LocationBase):

    code = models.CharField(_("Continent code"), max_length=2, db_index=True)

    class Meta:
        app_label = 'geoware'
        db_table = app_label + '-continent'
        unique_together = [('name', 'code')]

    @property
    def parent(self):
        return None


