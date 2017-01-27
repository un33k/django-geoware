from django.utils.translation import ugettext as _

from .base import models
from .base import AbstractLocation


class Division(AbstractLocation):
    """
    Division Model Class.
    """
    country = models.ForeignKey(
        'Country',
        verbose_name=_('Country'),
        related_name='%(app_label)s_%(class)s_country',
        null=True,
        blank=True,
    )

    capital = models.ForeignKey(
        'City',
        verbose_name=_("Capital"),
        related_name='%(app_label)s_%(class)s_capital',
        null=True,
        blank=True,
    )

    code = models.CharField(
        _('Code'),
        max_length=40,
        null=True,
        blank=True,
    )

    fips = models.CharField(
        _('FIPS'),
        max_length=40,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='division')
        verbose_name = _('Division')
        verbose_name_plural = _('Divisions')
        unique_together = [('fips', 'name_std', 'country')]

    @property
    def parent(self):
        if self.country:
            return self.country
        return None
