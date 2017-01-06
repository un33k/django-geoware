import os
import logging
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.db import transaction
from django.utils.encoding import smart_str

from ..base import GeoBaseCommand
from ...utils.downloader import *
from ...utils.updater import *
from ...utils.fetcher import *
from ...utils.fixer import *
from ...models import (City, Subregion, Region, Country)
from ... import defaults

if defaults.GEOWARE_USING_GIS:
    from django.contrib.gis.geos import Point

logger = logging.getLogger("geoware.cmd.city")


class Command(GeoBaseCommand):
    cmd_name = "City"

    def is_entry_valid(self, item):
        try:
            geoid = int(item[0])
            name = item[2]
            lat = item[4]
            lat = item[5]
            country_code = item[8]
        except:
            return False
        return True

    def get_query_kwargs(self, data):
        country = self._get_country_cache(data['country_code'])
        if country:
            return {'name': data['name'], 'country': country}
        return {}

    def create_or_update_entry(self, item):
        """ Save or update a given city entry into DB """

        data = self.record_to_dict(item)
        if not data:
            return

        city = self.get_geo_object(City, data)
        if not city:
            return

        if data['city_code'] not in defaults.GEOWARE_CITY_TYPES:
            return

        logger.debug("\n****************>>>\n{0}".format(item))

        city.geoname_id = data['geoid']
        if (not city.name_std) or self.overwrite: city.name_std = data['name_std']
        if (not city.name) or self.overwrite: city.name = data['name']
        if defaults.GEOWARE_USING_GIS:
            if (city.point.x == float(0) and city.point.y == float(0)) or self.overwrite: city.point = Point(data['latitude'], data['longitude'])
        else:
            if (not city.lat) or self.overwrite: city.lat = data['latitude']
            if (not city.lng) or self.overwrite: city.lng = data['longitude']
        if (not city.population) or self.overwrite: city.population = data['population'] if data['population'] > 0 else 0
        if (not city.elevation) or self.overwrite: city.elevation = data['elevation'] if data['elevation'] > 0 else 0

        if data['country_code']:
            city.country = self._get_country_cache(data['country_code'])
        if not city.country:
            return

        if data['region_code']:
            fips = '.'.join([data['country_code'], data['region_code']])
            region = self._get_region_cache(fips)
            if region:
                city.region = region

        if data['subregion_code']:
            fips = '.'.join([data['country_code'], data['region_code'], data['subregion_code']])
            subregion = self._get_subregion_cache(fips)
            if subregion:
                city.subregion = subregion

        if data['timezone']:
            timezone = self._get_timezone_cache(data['timezone'])
            if timezone:
                city.timezone = timezone

        city_pre_save_call(city)

        success, reason = self.save_to_db(city)
        if success:
            logger.debug("Added {0}: {1} ({2})({3})({4})".format(self.cmd_name, city, city.subregion, city.region, city.country))
            if self.is_capital(data):
                city.country.capital = city
                city.country.save()
        else:
            logger.error("Failed to add {0}: {1} ({2}) [{3}]".format(self.cmd_name, city, city.country, reason))


    def record_to_dict(self, item):
        """ Given a list of info for and entry, it returns a dict """

        get_field = lambda x,i: x[i] if len(x)>i else ''
        try:
            item = [smart_str(x) for x in item]
        except:
            pass
        dicts = {}
        try:
            dicts = {
                'geoid'             : get_field(item, 0),
                'name_std'          : smart_str(get_field(item, 1)),
                'name'              : smart_str(get_field(item, 2)),
                'latitude'          : float(get_field(item, 4) if get_field(item, 4) else 0),
                'longitude'         : float(get_field(item, 5) if get_field(item, 5) else 0),
                'city_code'         : get_field(item, 7),
                'country_code'      : get_field(item, 8),
                'region_code'       : get_field(item, 10),
                'subregion_code'    : get_field(item, 11),
                'population'        : float(get_field(item, 14) if get_field(item, 14) else 0),
                'elevation'         : float(get_field(item, 16) if get_field(item, 16) else 0),
                'timezone'          : get_field(item, 17),
            }
        except Exception as e:
            logger.warning("Failed to extract {0} data. {1}".format(self.cmd_name, item))
        return dicts

    def is_capital(self, data):
        if data['city_code'] in defaults.GEOWARE_CAPITAL_TYPES:
            return True
        return False





