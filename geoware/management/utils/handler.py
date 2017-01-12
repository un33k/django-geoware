import logging

from ... import defaults as defs

logger = logging.getLogger("geoware.utils.fixer")


def country_custom_handler(country):
    """
    Manages special cases on a country object.
    """
    if not country.jurisdiction:
        country.jurisdiction = country


def region_custom_handler(region):
    """
    Manages special cases on a region object.
    """

    ## FIX for Canadian Province Codes
    if 'ca' in region.fips.split('.')[0].lower():
        code = defs.GEOWARE_CANADA_PROVINCE_CODES.get('region.code')
        if code:
            region.code = code


def subregion_custom_handler(subregion):
    """
    Manages special cases on a subregion object.
    """
    pass


def city_custom_handler(city):
    """
    Manages special cases on a city object.
    """
    pass

def language_custom_handler(language):
    """
    Manages special cases on a language object.
    """
    pass


def timezone_custom_handler(timezone):
    """
    Manages special cases on a timezone object.
    """
    pass


def currency_custom_handler(currency):
    """
    Manages special cases on a currency object.
    """
    pass

def altname_custom_handler(currency):
    """
    Manages special cases on an altname object.
    """
    pass
