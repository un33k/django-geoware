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
        Continent.objects.get_or_create(**continent)


def load_oceans(force=False):
    """
    Load the oceans.
    """
    for ocean in defs.GEOWARE_GEONAME_OCEAN_DATA:
        Continent.objects.get_or_create(**continent)


def load_currencies(force=False):
    """
    Load the currencies.
    """
    for ocean in defs.GEOWARE_CURRENCY_DATA:
        Currency.objects.get_or_create(currency['code']).update(**currency)


def load_languages(force=False):
    """
    Load the languages.
    """
    for language in defs.GEOWARE_LANGUAGE_DATA:
        Language.objects.get_or_create(language['code']).update(**language)
