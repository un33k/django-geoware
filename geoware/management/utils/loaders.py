from ...models import Continent
from ...models import Ocean
from ...models import Currency
from ...models import Language
from ... import defaults as defs


def save_object_attrs(instance, data, created=False):
    """
    Given an instance and a data dictionary, it loads the data and saves the instance.
    """
    if not created:
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()


def load_continents():
    """
    Load the continents.
    """
    for data in defs.GEOWARE_GEONAME_CONTINENT_DATA:
        instance, created = Continent.objects.get_or_create(code=data['code'], defaults=data)
        save_object_attrs(instance, data, created)


def load_oceans(force=False):
    """
    Load the oceans.
    """
    for data in defs.GEOWARE_GEONAME_OCEAN_DATA:
        instance, created = Ocean.objects.get_or_create(name=data['name'], defaults=data)
        save_object_attrs(instance, data, created)


def load_currencies(force=False):
    """
    Load the currencies.
    """
    for currency, data in defs.GEOWARE_CURRENCY_DATA.items():
        instance, created = Currency.objects.get_or_create(code=data['code'], defaults=data)
        save_object_attrs(instance, data, created)


def load_languages(force=False):
    """
    Load the languages.
    """
    for data in defs.GEOWARE_LANGUAGE_DATA:
        instance, created = Language.objects.get_or_create(code=data['code'], defaults=data)
        save_object_attrs(instance, data, created)
