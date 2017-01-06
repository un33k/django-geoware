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
from ...models import (District, City, Subregion, Region, Country)
from ... import defaults

if defaults.GEOWARE_USING_GIS:
    from django.contrib.gis.geos import Point

logger = logging.getLogger("geoware.cmd.district")

class Command(GeoBaseCommand):
    cmd_name = "District"
    required_file = "City"
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
        return {'name': data['name'], 'geoname_id': data['geoid']}
        return {}

    def create_or_update_entry(self, item):
        """ Save or update a given entry into DB """

        data = self.record_to_dict(item)
        if not data:
            return

        district = self.get_geo_object(District, data)
        if not district:
            return

        if data['city_code'] not in defaults.GEOWARE_DISTRICT_TYPES:
            return

        logger.debug("\n****************>>>\n{0}".format(item))

        district.geoname_id = data['geoid']
        if (not district.name_std) or self.overwrite: district.name_std = data['name_std']
        if (not district.name) or self.overwrite: district.name = data['name']
        if defaults.GEOWARE_USING_GIS:
            if (district.point.x == float(0) and district.point.y == float(0)) or self.overwrite: district.point = Point(data['latitude'], data['longitude'])
        else:
            if (not district.lat) or self.overwrite: district.lat = data['latitude']
            if (not district.lng) or self.overwrite: district.lng = data['longitude']
        if (not district.population) or self.overwrite: district.population = data['population'] if data['population'] > 0 else 0
        if (not district.elevation) or self.overwrite: district.elevation = data['elevation'] if data['elevation'] > 0 else 0

        if data['timezone']:
            timezone = self._get_timezone_cache(data['timezone'])
            if timezone:
                district.timezone = timezone

        parent_city_id = self._get_hierarchy_cache(data['geoid'])
        parent_city = self._get_city_cache(parent_city_id)
        if not parent_city:
            parent_city = self._get_parent_city(data['latitude'], data['longitude'], data['country_code'])
        if not parent_city:
            return

        district.city = parent_city
        district_pre_save_call(district)

        success, reason = self.save_to_db(district)
        if success:
            logger.debug("Added {0}: {1} ({2})({3})".format(self.cmd_name, district, district.city, district.city.country if district.city else ''))
        else:
            logger.error("Failed to add {0}: {1} ({2}) [{3}]".format(self.cmd_name, district.city, district.city.country if district.city else '', reason))


    def record_to_dict(self, item):
        """ Given a list of info for an entry, it returns a dict """

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


    def post_download_call(self):
        """ Hierarchy file is downloaded, load it up """

        if not hasattr(self, '_hierarchy_cache'):
            self._hierarchy_cache = {}
            with open(self.local_file, encoding='utf-8') as afile:
                data = afile.read().splitlines()
                for item in parse_data(data):
                    parent, child = item[0], item[1]
                    self._hierarchy_cache[child] = parent

        self.rfile = defaults.GEOWARE_FILE_DICT[self.required_file.lower()]['url'].format(filename=defaults.GEOWARE_FILE_DICT[self.required_file.lower()]['filename'])


    def _get_hierarchy_cache(self, geonames_id):
        """ Given a geoname ID of a child, it returns a goename ID of parent from cache """

        if hasattr(self, '_hierarchy_cache'):
            try:
                return self._hierarchy_cache[geonames_id]
            except:
                pass
        return None


    def _get_parent_city(self, lat, lng, country_code, city_pop_min=50000):
        """ Get a parnet city for a district """

        city = None
        if defaults.GEOWARE_USING_GIS:
            try:
                city = City.objects.filter(population__gt=city_pop_min).distance(Point(lat, lng)).order_by('distance')[0]
            except:
                pass

        if not city:
            try:
                from geopy import distance
            except:
                return None
            cities = list(City.objects.filter(country__code=country_code, population__gt=city_pop_min))
            if not cities:
                return None
            for city in cities:
                city.distance = distance.VincentyDistance((lat, lng),(city.lat, city.lng)).km
            cities.sort(key=lambda x: x.distance)
            city = cities[0]
        return city



