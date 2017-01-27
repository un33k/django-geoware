from django.utils.translation import ugettext as _

from .base import models
from .base import AbstractLocation


class Subdivision(AbstractLocation):
    """
    Subdivision Model Class.
    """
    division = models.ForeignKey(
        'Division',
        verbose_name=_('Division'),
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
        'FIPS',
        max_length=40,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='subdivision')
        verbose_name = _('Subdivision')
        verbose_name_plural = _('Subdivisions')
        unique_together = [('name', 'fips', 'division')]

    @property
    def parent(self):
        return self.division
