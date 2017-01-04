from django.utils.translation import ugettext_lazy as _

from .base import models
from .base import AbstractLocation


class Region(AbstractLocation):
    """
    Region Model Class.
    """
    country = models.ForeignKey(
        'Country',
        _('LOCATION.REGION.COUNTRY')
        related_name='%(app_label)s_%(class)s_country',
        null=True,
        blank=True,
    )

    capital = models.ForeignKey(
        'City',
        _("LOCATION.REGION.CAPITAL"),
        related_name='%(app_label)s_%(class)s_capital',
        null=True,
        blank=True,
    )

    code = models.CharField(
        _('LOCATION.REGION.CODE'),
        max_length=40,
        null=True,
        blank=True,
    )

    code = models.CharField(
        _('LOCATION.REGION.CODE_FIPS'),
        max_length=40,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='region')
        verbose_name = _('LOCATION.REGION')
        verbose_name_plural = _('LOCATION.REGION#plural')
        unique_together = [('name', 'country')]

   @property
    def parent(self):
        if self.country:
            return self.country
        return None
