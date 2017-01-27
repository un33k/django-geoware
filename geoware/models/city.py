from django.utils.translation import ugettext as _

from .base import models
from .base import AbstractCity


class City(AbstractCity):

    country = models.ForeignKey(
        'Country',
        verbose_name=_('Country'),
        related_name='%(app_label)s_%(class)s_country',
        null=True,
        blank=True,
    )

    division = models.ForeignKey(
        'Division',
        verbose_name=_('Division'),
        related_name='%(app_label)s_%(class)s_division',
        blank=True,
        null=True,
    )

    subdivision = models.ForeignKey(
        'Subdivision',
        verbose_name=_('Subdivision'),
        related_name='%(app_label)s_%(class)s_subdivision',
        blank=True,
        null=True,
    )

    timezone = models.ForeignKey(
        'Timezone',
        verbose_name=_('Timezone'),
        related_name='%(app_label)s_%(class)s_timezone',
        blank=True,
        null=True,
    )

    district_of = models.ForeignKey(
        'self',
        verbose_name=_('District Of'),
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='city')
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        unique_together = (('name', 'division', 'country'), )

    @property
    def parent(self):
        if self.district_of and self.district_of.parent:
            return self.district_of
        elif self.subdivision and self.subdivision.parent:
            return self.subdivision
        elif self.division and self.division.parent:
            return self.division
        elif self.country and self.country.parent:
            return self.country
        return None
