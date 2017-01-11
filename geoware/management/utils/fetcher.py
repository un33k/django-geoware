import logging
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
from django.contrib.sites.models import Site

from ...models import *

logger = logging.getLogger("geoware.utils.fetcher")


def get_language_objects(lang_list=[]):
    """ Given a list of language codes (str), it returns the objects """

    languages = []
    if lang_list:
        for code in lang_list:
            if code:
                l = get_language_by_code(code)
                if l:
                    languages.append(l)
    return languages


def get_language_by_code(code):
    """ Given a valid language code, returns a language object """

    language = None
    try:
        language = Language.objects.get(code__iexact=code.strip())
    except ObjectDoesNotExist:
        pass
    except Exception as err:
        logger.error("Error getting language by code: {0} - {1}".format(code, err))
        pass
    return language


def get_country_objects(country_list=[]):
    """ Given a list of country codes (str), it returns the objects """

    countries = []
    if country_list:
        for code in country_list:
            if code:
                c = get_country_by_code(code)
                if c:
                    countries.append(c)
    return countries


def get_country_by_code(code):
    """ Given a valid country code, retunrs a country object """
    country = None
    try:
        country = Country.objects.get(code__iexact=code.strip())
    except ObjectDoesNotExist:
        pass
    except Exception as err:
        logger.error("Error getting country by code: {0} - {1}".format(code, err))
        pass
    return country


def get_region_by_fips(fips):
    """ Given a valid region fips code, returns a region object """
    region = None
    try:
        region = Region.objects.get(fips__iexact=fips.strip())
    except ObjectDoesNotExist:
        pass
    except Exception as e:
        logger.error("Error getting region by code: {0} - {1}".format(fips, err))
        pass
    return region


def get_subregion_by_fips(fips):
    """ Given a valid subregion fips code, returns a subregion object """
    subregion = None
    try:
        subregion = Subregion.objects.get(fips__iexact=fips.strip())
    except ObjectDoesNotExist:
        pass
    except Exception as err:
        logger.error("Error getting subregion by code: {0} - {1}".format(fips, err))
        pass
    return subregion


def get_timezone_by_name_id(name):
    """ Given a valid timezone name, returns a timezone object """
    timezone = None
    try:
        timezone = Timezone.objects.get(name_id__iexact=name.strip())
    except ObjectDoesNotExist:
        pass
    except Exception as err:
        logger.error("Error getting timezone by name id: {0} - {1}".format(name, err))
        pass
    return timezone


def get_country_list(cache_time=86400):
    site = Site.objects.get_current()
    key = '{0}_geoware_country_cache_key'.format(site.domain)
    countries = cache.get(key)
    if not countries:
        countries = Country.objects.filter(is_active=True).order_by('name')
        cache.set(key, list(countries), cache_time)
    return countries


def get_continent_list(cache_time=86400):
    site = Site.objects.get_current()
    key = '{0}_geoware_continet_cache_key'.format(site.domain)
    continents = cache.get(key)
    if not continents:
        continents = Continent.objects.filter(is_active=True).order_by('name')
        cache.set(key, list(continents), cache_time)
    return continents



def get_countries_by_codes(self, code_list):
    """
    Given a `,` separated string of country codes,
    Returns: a list of objects to all countries.
    If country is not found, it creates it.
    """
    countries = []
    for code in code_list.split(','):
        if code:
            try:
                country, created = Country.objects.get_or_create(code__iexact=code)
            except Country.MultipleObjectsReturned:
                Country.objects.filter(code__iexact=code).delete()
                country, created = Country.objects.get_or_create(code__iexact=code)
            countries.append(country)

    return countries


