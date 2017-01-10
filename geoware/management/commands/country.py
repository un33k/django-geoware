import os
import logging

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ..base import GeoBaseCommand
from ...utils.common import *
from ...utils.updater import *
from ...utils.fetcher import *
from ...models import Country
from ...models import Continent
from ...models import Language
from ...models import Currency

logger = logging.getLogger("geoware.cmd.country")


class Command(GeoBaseCommand):
    cmd_name = "country"

    def is_entry_valid(self, item):
        """
        Checks for minimum country requirements.
        """
        is_valid = True
        try:
            code = item[0]
            name = item[4]
            geoid = int(item[16])
        except:
            is_valid = False

        if is_valid and code and name:
            return is_valid

        logger.warning("Invalid Record: ({item})".format(item=item))
        return False

    def get_query_kwargs(self, data):
        """
        Minimum unique data to identify record.
        """
        kwargs = {'code': data['code']}
        return kwargs

    def record_to_dict(self, item):
        """
        Given a country record, it returns a dictionary.
        """
        dicts = {}
        try:
            dicts = {
                'code'            : get_str(item, 0),
                'iso_3'           : get_str(item, 1),
                'iso_n'           : get_str(item, 2),
                'fips'            : get_str(item, 3),
                'name'            : get_str(item, 4),
                'captial'         : get_str(item, 5),
                'area'            : get_float(item, 6),
                'population'      : get_int(item, 7),
                'continent_code'  : get_str(item, 8),
                'tld'             : get_str(item, 9).strip('.'),
                'currency_code'   : get_str(item, 10),
                'currency_name'   : get_str(item, 11),
                'idc'             : get_str(item, 12),
                'postal_format'   : get_str(item, 13),
                'postal_regex'    : get_str(item, 14),
                'languages'       : get_str(item, 15),
                'geoid'           : get_str(item, 16),
                'neighbors'       : get_str(item, 17),
                'altfips'         : get_str(item, 18),
            }
        except Exception as err:
            logger.warning("Failed to extract {cmd} data. {record} {err}".format(cmd=self.cmd_name, record=item, err=err))
        return dicts

    def create_or_update_record(self, item):
        """
        Create or update a given entry into DB
        """
        data = self.record_to_dict(item)
        if not data:
            return

        country, created = self.get_geo_object(Country, data)
        if not country or (not created and not self.overwrite):
            return

        logger.debug("\n****************>>>\n{item}".format(item=item))

        country.geoname_id = data.get('geoid')
        country.name = data.get('name', country.name)
        country.code = data.get('code', country.code)
        country.iso_3 = data.get('iso_3', country.iso_3)
        country.iso_n = data.get('iso_n', country.iso_n)
        country.fips = data.get('fips', country.fips)
        country.area = data.get('area', country.area)
        country.population = data.get('population', country.population)
        country.tld = data.get('tld', country.tld)
        country.idc = data.get('idc', country.idc)

        if data.get('continent_code'):
            cont = self._get_continent_cache(data['continent_code'])
            country.continent = cont

        if data.get('currency_code'):
            curr = self._get_currency_cache(data['currency_code'])
            country.currency = curr

        if not country.jurisdiction:
            country.jurisdiction = country

        country.save()

        if data.get('languages'):
            country.languages.clear()
            lang_list = []
            for l in data['languages'].split(','):
                lang = self._get_language_cache(l.strip())
                if lang:
                    lang_list.append(lang)
            if lang_list:
                for language in lang_list:
                    country.languages.add(language)

        if data.get('neighbors'):
            country.neighbors.clear()
            neighbors = self._get_neighbors(data['neighbors'])
            if neighbors:
                for neighbor in neighbors:
                    country.neighbors.add(neighbor)

    def _get_neighbors(self, country_codes):
        """
        Given a `,` separated string of country codes, returns the a list of objects to all countries.
        """
        neighbors = []
        for code in country_codes.split(','):
            if code:
                try:
                    country, created = Country.objects.get_or_create(code__iexact=code)
                except Country.MultipleObjectsReturned:
                    Country.objects.filter(code__iexact=code).delete()
                    country, created = Country.objects.get_or_create(code__iexact=code)
                neighbors.append(country)

        return neighbors


    def post_load_call(self):
        """
        Clean up countries with empty names.
        """
        Country.objects.filter(name__exact='').delete()
