import os
import logging
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.utils.encoding import smart_str

from ..base import GeoBaseCommand
from ...utils.downloader import *
from ...utils.updater import *
from ...utils.fetcher import *
from ...models import (Country, Continent, Language, Currency)

logger = logging.getLogger("geoware.cmd.country")

class Command(GeoBaseCommand):
    help = "usage: %prog <--download> | <--load> [--force]"
    cmd_name = "Country"

    def is_entry_valid(self, item):
        try:
            name = item[4]
            geoid = int(item[16])
        except:
            return False
        return True

    def get_query_kwargs(self, data):
        kwargs = {'code': data['code']}
        return kwargs

    def save_or_update_entry(self, item):
        """ Save or update a given entry into DB """

        data = self.entry_to_dict(item)
        if not data:
            return

        country = self.get_geo_object(Country, data)
        if not country:
            return

        logger.debug("\n****************>>>\n{0}".format(item))

        country.geoname_id = data['geoid']
        if (not country.code) or self.overwrite: country.code = data['code']
        if (not country.iso_3) or self.overwrite: country.iso_3 = data['iso_3']
        if (not country.iso_n) or self.overwrite: country.iso_n = data['iso_n']
        if (not country.fips) or self.overwrite: country.fips = data['fips']
        if (not country.name) or self.overwrite: country.name = data['name']
        if (not country.area) or self.overwrite: country.area = data['area'] if data['area'] > 0 else 0
        if (not country.population) or self.overwrite: country.population = data['population'] if data['population'] > 0 else 0
        if (not country.tld) or self.overwrite: country.tld = data['tld']
        if (not country.idc) or self.overwrite: country.idc = data['idc']

        if data['continent_code']:
            cont = self._get_continent_cache(data['continent_code'])
            country.continent = cont

        if ((not country.currency) or self.overwrite) and data['currency_code']:
            curr = self._get_currency_cache(data['currency_code'])
            country.currency = curr

        if not country.jurisdiction:
            country.jurisdiction = country

        success, reason = self.save_to_db(country)
        if success:
            logger.debug("Added {0}: {1} ({2})".format(self.cmd_name, country, country.code))
        else:
            logger.error("Failed to add {0}: {1} ({2}) [{3}]".format(self.cmd_name, country, country.code, reason))
            return

        if (country.languages.all().count() == 0 or self.overwrite) and data['languages']:
            country.languages.clear()
            lang_list = []
            for l in data['languages'].split(','):
                lang = self._get_language_cache(l.strip())
                if lang:
                    lang_list.append(lang)
            if lang_list:
                country.languages.add(*lang_list)
                logger.debug("Added languages to {0}: {1} ({2})".format(self.cmd_name, country, ', '.join([l.name for l in lang_list])))

        if (country.neighbours.all().count() == 0 or self.overwrite) and data['neighbours']:
            country.neighbours.clear()
            neighbours = self._get_neighbours([c.strip() for c in data['neighbours'].split(',')])
            if neighbours:
                country.neighbours.add(*neighbours)

    def entry_to_dict(self, item):
        """ Given a list of info for an entry, it returns a dict """

        get_field = lambda x,i: x[i] if len(x)>i else ''
        try:
            item = [force_unicode(x) for x in item]
        except:
            pass
        dicts = {}
        try:
            dicts = {
                'code'           : get_field(item, 0),
                'iso_3'           : get_field(item, 1),
                'iso_n'           : get_field(item, 2),
                'fips'            : get_field(item, 3),
                'name'            : smart_str(get_field(item, 4)),
                'captial'         : get_field(item, 5),
                'area'            : float(get_field(item, 6)) if get_field(item, 6) else 0,
                'population'      : float(get_field(item, 7)) if get_field(item, 7) else 0,
                'continent_code'  : get_field(item, 8),
                'tld'             : get_field(item, 9).strip('.'),
                'currency_code'   : get_field(item, 10),
                'currency_name'   : get_field(item, 11),
                'idc'             : get_field(item, 12),
                'postal_format'   : get_field(item, 13),
                'postal_regex'    : get_field(item, 14),
                'languages'       : get_field(item, 15),
                'geoid'           : get_field(item, 16),
                'neighbours'      : get_field(item, 17),
                'altfips'         : get_field(item, 18),
            }
        except Exception, e:
            logger.warning("Failed to extract {0} data. {1} {2}".format(self.cmd_name, item, e))
        return dicts

    def _get_neighbours(self, neighbours_country_code):
        """ Given a country code and a lis to neighbouring country codes, it returns neighbours obj """

        neighbours = []
        for neighbour_code in neighbours_country_code:
            try:
                country = Country.objects.get(code__iexact=neighbour_code)
            except Country.DoesNotExist:
                country = Country(code=neighbour_code)
                country.save()
            except:
                continue
            if country:
                neighbours.append(country)
        return neighbours


    def post_load_call(self):
        """ Clean up countries with empty names """

        try:
            Country.objects.filter(name__exact='').delete()
        except:
            pass



