from django.utils.translation import ugettext as _

from .base import models
from .base import AbstractLocation


class Country(AbstractLocation):
    """
    Country Model Class.
    """
    continent = models.ForeignKey(
        'Continent',
        verbose_name=_('Continent'),
        related_name='%(app_label)s_%(class)s_continent',
        null=True,
        blank=True,
    )

    jurisdiction = models.ForeignKey(
        'Country',
        verbose_name=_('Jurisdiction'),
        related_name='%(app_label)s_%(class)s_jurisdiction',
        blank=True,
        null=True,
        help_text=_('Sovereignty'),
    )

    currency = models.ForeignKey(
        'Currency',
        verbose_name=_('Currency'),
        related_name='%(app_label)s_%(class)s_currency',
        blank=True,
        null=True,
    )

    capital = models.ForeignKey(
        'City',
        verbose_name=_('Capital'),
        related_name='%(app_label)s_%(class)s_capital',
        blank=True,
        null=True,
    )

    code = models.CharField(
        'ISO 3166-1',
        db_index=True,
        max_length=2,
    )

    iso_3 = models.CharField(
        'ISO 3166-2',
        db_index=True,
        max_length=3,
    )

    iso_n = models.CharField(
        'M49',
        db_index=True,
        max_length=40,
    )

    fips = models.CharField(
        'FIPS',
        db_index=True,
        max_length=40,
    )

    idc = models.CharField(
        _('International Dialing Code'),
        max_length=40,
        null=True,
        blank=True,
    )

    tld = models.CharField(
        _('Top Level Domain'),
        max_length=2,
        null=True,
        blank=True,
    )

    neighbors = models.ManyToManyField(
        'self',
        verbose_name=_('Neighbors'),
        related_name='%(app_label)s_%(class)s_neighbors',
        blank=True,
    )

    languages = models.ManyToManyField(
        'Language',
        verbose_name=_('Languages'),
        related_name='%(app_label)s_%(class)s_languagues',
        blank=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='country')
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        unique_together = (('code'), )

    @property
    def parent(self):
        if self.continent:
            return self.continent
        return None
