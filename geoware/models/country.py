
from django.db import models
from django.utils.translation import gettext as _
from base import LocationBase

__all__ = ['Country']

class Country(LocationBase):
    continent = models.ForeignKey('Continent', related_name='%(app_label)s_%(class)s_continent', null=True, blank=True)
    jurisdiction = models.ForeignKey('Country', help_text=_('Sovereignty'), related_name='%(app_label)s_%(class)s_jurisdiction', blank=True, null=True)
    currency = models.ForeignKey('Currency', related_name='%(app_label)s_%(class)s_currency', blank=True, null=True)
    capital = models.ForeignKey('City', related_name='%(app_label)s_%(class)s_capital', blank=True, null=True)
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
        return self.continent





