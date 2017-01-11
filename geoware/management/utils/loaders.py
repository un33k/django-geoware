from ...models import Continent
from ...models import Ocean
from ...models import Currency
from ...models import Language
from ... import defaults as defs


def load_continents(force=False):
    """
    Load the continents.
    """
    for continent in defs.GEOWARE_GEONAME_CONTINENT_DATA:
        Continent.objects.get_or_create(code=continent['code'], defaults=continent)


def load_oceans(force=False):
    """
    Load the oceans.
    """
    for ocean in defs.GEOWARE_GEONAME_OCEAN_DATA:
        Ocean.objects.get_or_create(name=ocean['name'], defaults=ocean)


def load_currencies(force=False):
    """
    Load the currencies.
    """
    for currency in defs.GEOWARE_CURRENCY_DATA:
        Currency.objects.get_or_create(code=currency['code'], defaults=currency)


def load_languages(force=False):
    """
    Load the languages.
    """
    for language in defs.GEOWARE_LANGUAGE_DATA:
        Language.objects.get_or_create(code=language['code'], defaults=language)
