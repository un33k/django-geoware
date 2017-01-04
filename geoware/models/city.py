from django.utils.translation import ugettext_lazy as _

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

    region = models.ForeignKey(
        'Region',
        verbose_name=_('LOCATION.CITY.REGION'),
        related_name='%(app_label)s_%(class)s_region',
        blank=True,
        null=True,
    )

    subregion = models.ForeignKey(
        'Subregion',
        verbose_name=_('LOCATION.CITY.SUBREGION'),
        related_name='%(app_label)s_%(class)s_subregion',
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

    sister = models.ForeignKey(
        'City',
        verbose_name=_('LOCATION.CITY.SISTER'),
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='city')
        verbose_name = _('LOCATION.CITY')
        verbose_name_plural = _('LOCATION.CITY#plural')

    @property
    def parent(self):
        if self.subregion and self.subregion.parent:
            return self.subregion
        elif self.region and self.region.parent:
            return self.region
        elif self.country and self.country.parent:
            return self.country
        return None



