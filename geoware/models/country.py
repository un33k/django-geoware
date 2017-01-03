from django.utils.translation import ugettext_lazy as _

from .base import models
from .base import AbstractLocation


class Country(LocationBase):
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
        help_text=_('LOCATION.COUNTRY.SOVEREGNTY'),
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
        related_name='%(app_label)s_%(class)s_capital',
        blank=True,
        null=True,
    )

    code = models.CharField(_('ISO alpha-2'), max_length=2, db_index=True)
    iso_3 = models.CharField(_('ISO alpha-3'), max_length=3, blank=True, null=True)
    iso_n = models.CharField(_('ISO numeric'), max_length=40, blank=True, null=True)
    fips = models.CharField(_('FIPS code'), max_length=40, blank=True, null=True)
    idc = models.CharField(_('International dialing code'), max_length=40, null=True, blank=True)
    tld = models.CharField(_('Top level domain code'), max_length=2, null=True, blank=True)
    neighbours = models.ManyToManyField('self', help_text=_('Neighbouring countries'), related_name='%(app_label)s_%(class)s_neighbours', blank=True, null=True)
    languages = models.ManyToManyField('Language', help_text=_('Languages'),  related_name='%(app_label)s_%(class)s_languagues', blank=True, null=True)

    class Meta:
        app_label = 'geoware'
        db_table = app_label + '-country'
        verbose_name = _('country')
        verbose_name_plural = _('countries')

    @property
    def parent(self):
        if self.continent:
            return self.continent
        return None





