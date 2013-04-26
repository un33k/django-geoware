from ..models import *
from .. import defaults

def import_continents(force=False):
    if not Continent.objects.count():
        force = True
    for continent in defaults.GEOWARE_CONTINENT_CHOICES:
        try:
            obj = Continent.objects.get(code__iexact=continent[0])
            if not force: return
        except Continent.DoesNotExist:
            obj = Continent(code=continent[0])
        if obj:
            obj.name = continent[1]
            obj.save()


def import_oceans(force=False):
    if not Ocean.objects.count():
        force = True
    for ocean in defaults.GEOWARE_OCEAN_CHOICES:
        try:
            obj = Ocean.objects.get(name__iexact=ocean[1])
            if not force: return
        except Ocean.DoesNotExist:
            obj = Ocean(name=ocean[1])
        if obj:
            obj.name = ocean[1]
            obj.save()


def import_currencies(force=False):
    if not Currency.objects.count():
        force = True
    for currency in defaults.GEOWARE_CURRENCY_CHOICES:
        try:
            obj = Currency.objects.get(code__iexact=defaults.GEOWARE_CURRENCY_CHOICES[currency]['code'])
            if not force: return
        except Currency.DoesNotExist:
            obj = Currency(code=defaults.GEOWARE_CURRENCY_CHOICES[currency]['code'])
        if obj:
            obj.name = defaults.GEOWARE_CURRENCY_CHOICES[currency]['name']
            obj.symbol = defaults.GEOWARE_CURRENCY_CHOICES[currency]['symbol']
            obj.fractional_unit = defaults.GEOWARE_CURRENCY_CHOICES[currency]['fractional_unit']
            obj.fractional_ratio = defaults.GEOWARE_CURRENCY_CHOICES[currency]['fractional_ratio']
            obj.save()


def import_languages(force=False):
    if not Language.objects.count():
        force = True
    for language in defaults.GEOWARE_LANGUAGE_CHOICES:
        try:
            obj = Language.objects.get(code__iexact=language[0])
            if not force: return
        except Language.DoesNotExist:
            obj = Language(code=language[0])
        if obj:
            name_dialect = language[1].split('(')
            obj.name = name_dialect[0].strip()
            if len(name_dialect) > 1:
                obj.dialect = name_dialect[1].strip(")").strip()
            obj.save()




