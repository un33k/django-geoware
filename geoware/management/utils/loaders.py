from django.db import transaction
from django.db import IntegrityError

from ...models import Continent
from ...models import Ocean
from ...models import Currency
from ...models import Language
from ... import defaults as defs


def save_object_attrs(instance, data):
    """
    Given an instance and a data dictionary, it loads the data and saves the instance.
    """
    for attr, value in data.items():
        setattr(instance, attr, value)
    instance.save()


def load_continents():
    """
    Load the continents.
    """
    for data in defs.GEOWARE_GEONAME_CONTINENT_DATA:
        try:
            with transaction.atomic():
                instance, created = Continent.objects.get_or_create(code=data['code'])
        except IntegrityError:
            instance = Continent(code=data['code'])

        save_object_attrs(instance, data)
        instance.save()


def load_oceans(force=False):
    """
    Load the oceans.
    """
    for data in defs.GEOWARE_GEONAME_OCEAN_DATA:
        try:
            with transaction.atomic():
                instance, created = Ocean.objects.get_or_create(name=data['name'])
        except IntegrityError:
            instance = Ocean(name=data['name'])

        save_object_attrs(instance, data)
        instance.save()


def load_currencies(force=False):
    """
    Load the currencies.
    """
    for currency, data in defs.GEOWARE_CURRENCY_DATA.items():
        try:
            with transaction.atomic():
                instance, created = Currency.objects.get_or_create(code=data['code'])
        except IntegrityError:
            instance = Currency(code=data['code'])

        save_object_attrs(instance, data)
        instance.save()


def load_languages(force=False):
    """
    Load the languages.
    """
    for data in defs.GEOWARE_LANGUAGE_DATA:
        try:
            with transaction.atomic():
                instance, created = Language.objects.get_or_create(code=data['code'])
        except IntegrityError:
            instance = Language(code=data['code'])

        save_object_attrs(instance, data)
        instance.save()
