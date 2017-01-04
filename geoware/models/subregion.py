from django.utils.translation import ugettext as _

from .base import models
from .base import AbstractLocation


class Subregion(AbstractLocation):
    """
    Subregion Model Class.
    """
    region = models.ForeignKey(
        'Region',
        verbose_name=_('LOCATION.SUBREGION.REGION'),
        related_name='%(app_label)s_%(class)s_country',
        null=True,
        blank=True,
    )

    capital = models.ForeignKey(
        'City',
        verbose_name=_("LOCATION.SUBREGION.CAPITAL"),
        related_name='%(app_label)s_%(class)s_capital',
        null=True,
        blank=True,
    )

    code = models.CharField(
        _('LOCATION.SUBREGION.CODE'),
        max_length=40,
        null=True,
        blank=True,
    )

    fips = models.CharField(
        _('LOCATION.SUBREGION.CODE_FIPS'),
        max_length=40,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='subregion')
        verbose_name = _('LOCATION.SUBREGION')
        verbose_name_plural = _('LOCATION.SUBREGION#plural')
        unique_together = [('name', 'region')]

    @property
    def parent(self):
        return self.region
