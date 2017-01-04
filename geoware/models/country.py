from django.utils.translation import ugettext_lazy as _

from .base import models
from .base import AbstractLocation


class Country(AbstractLocation):
    """
    Country Model Class.
    """
    continent = models.ForeignKey(
        'Continent',
        _('LOCATION.COUNTRY.CONTINENT')
        related_name='%(app_label)s_%(class)s_continent',
        null=True,
        blank=True,
    )

    jurisdiction = models.ForeignKey(
        'Country',
        _('LOCATION.COUNTRY.JURISDICTION')
        related_name='%(app_label)s_%(class)s_jurisdiction',
        blank=True,
        null=True,
        help_text=_('LOCATION.COUNTRY.SOVEREIGNTY'),
    )

    currency = models.ForeignKey(
        'Currency',
        _('LOCATION.CURRENCY')
        related_name='%(app_label)s_%(class)s_currency',
        blank=True,
        null=True,
    )

    capital = models.ForeignKey(
        'City',
        _('LOCATION.CAPTIAL')
        related_name='%(app_label)s_%(class)s_capital',
        blank=True,
        null=True,
    )

    code = models.CharField(
        _('LOCATION.CODE.ISO_ALPHA_2'),
        db_index=True,
        max_length=2,
    )

    iso_3 = models.CharField(
        _('LOCATION.CODE.ISO_ALPHA_3'),
        db_index=True,
        max_length=3,
    )

    iso_n = models.CharField(
        _('LOCATION.CODE.ISO_NUMERIC'),
        db_index=True,
        max_length=40,
    )

    fips = models.CharField(
        _('LOCATION.CODE.FIPS'),
        db_index=True,
        max_length=40,
    )

    idc = models.CharField(
        _('LOCATION.CODE.INTERNATIONAL_DIALING'),
        max_length=40,
        null=True,
        blank=True,
    )

    tld = models.CharField(
        _('LOCATION.CODE.TOP_LEVEL_DOMAIN'),
        max_length=2,
        null=True,
        blank=True,
    )

    neighbours = models.ManyToManyField(
        'self',
        _('LOCATION.COUNTRY.NEIGHBORS'),
        related_name='%(app_label)s_%(class)s_neighbors',
        blank=True,
        null=True,
    )

    languages = models.ManyToManyField(
        'Language',
        _('LOCATION.LANGUAGUES'),
        related_name='%(app_label)s_%(class)s_languagues',
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='country')
        verbose_name = _('LOCATION.COUNTRY')
        verbose_name_plural = _('LOCATION.COUNTRY#plural')

    @property
    def parent(self):
        if self.continent:
            return self.continent
        return None





