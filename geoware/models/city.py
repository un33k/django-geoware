from django.utils.translation import ugettext as _

from .base import models
from .base import AbstractCity


class City(AbstractCity):

    country = models.ForeignKey(
        'Country',
        verbose_name=_('LOCATION.CITY.COUNTRY'),
        related_name='%(app_label)s_%(class)s_country',
        null=True,
        blank=True,
    )

    division = models.ForeignKey(
        'Division',
        verbose_name=_('LOCATION.CITY.DIVISION'),
        related_name='%(app_label)s_%(class)s_division',
        blank=True,
        null=True,
    )

    subdivision = models.ForeignKey(
        'Subdivision',
        verbose_name=_('LOCATION.CITY.SUBDIVISION'),
        related_name='%(app_label)s_%(class)s_subdivision',
        blank=True,
        null=True,
    )

    timezone = models.ForeignKey(
        'Timezone',
        verbose_name=_('LOCATION.CITY.TIMEZONE'),
        related_name='%(app_label)s_%(class)s_timezone',
        blank=True,
        null=True,
    )

    district_of = models.ForeignKey(
        'self',
        verbose_name=_('LOCATION.CITY.DISTRICT_OF'),
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='city')
        verbose_name = _('LOCATION.CITY')
        verbose_name_plural = _('LOCATION.CITY#plural')
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
