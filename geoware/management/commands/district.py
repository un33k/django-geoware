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
    cmd_name = "district"
    required_file = "City"

    def is_entry_valid(self, item):
        """
        Checks for minimum subregion requirements.
        """
        is_valid = True
        try:
            geoid = int(item[0])
            name = item[2]
            lat = item[4]
            lat = item[5]
            country_code = item[8]
        except:
            is_valid = False

        if is_valid and name and lat and lng and len(country_code) == 2:
            return is_valid

        logger.warning("Invalid Record: ({item})".format(item=item))
        return False

    def get_query_fields(self, data):
        """
        Fields to identify a region record.
        """
        fields = {'name': data['name'], 'geoname_id': data['geoid']}
        return fields

    def record_to_dict(self, item):
        """
        Given a district record, it returns a dictionary.
        """
        dicts = {}
        try:
            dicts = {
                'geoid'             : get_str(item, 0),
                'name_std'          : get_str(item, 1),
                'name'              : get_str(item, 2),
                'latitude'          : get_float(item, 4),
                'longitude'         : get_float(item, 5),
                'city_code'         : get_str(item, 7),
                'country_code'      : get_str(item, 8),
                'region_code'       : get_str(item, 10),
                'subregion_code'    : get_str(item, 11),
                'population'        : get_int(item, 14),
                'elevation'         : get_float(item, 16),
                'timezone'          : get_str(item, 17),
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

        if data.get('city_code') not in defaults.GEOWARE_CITY_TYPES:
            return

        parent_city_id = self._get_hierarchy_cache(data['geoid'])
        parent_city = self._get_city_cache(parent_city_id)
        if not parent_city:
            parent_city = self._get_parent_city(data['latitude'], data['longitude'], data['country_code'])
        if not parent_city:
            return

        if data.get('country_code'):
            country = self._get_country_cache(data['country_code'])
            if not country:
                return

        district, created = self.get_geo_object(District, data)
        if not district or (not created and not self.overwrite):
            return

        logger.debug("{action} District: {item}".format(action="Added" if created else "Updated", item=item))

        district.geoname_id = data.get('geoid')
        district.name = data.get('name', city.name)
        district.name_std = data.get('name_std', city.name_std)
        district.elevation = data.get('elevation', city.elevation)
        district.population = data.get('population', city.population)

        if defaults.GEOWARE_USING_GIS:
            district.point = Point(data['latitude'], data['longitude'])
        else:
            district.lat = data.get('lat', city.lat)
            district.lng = data.get('lng', city.lng)

        if data.get('timezone'):
            timezone = self._get_timezone_cache(data['timezone'])
            if timezone:
                city.timezone = timezone

        district.city = parent_city
        district_pre_save_call(district)
        district.save()

    def post_download_call(self):
        """
        Hierarchy file is downloaded, load it up for speed.
        """
        if not hasattr(self, '_hierarchy_cache'):
            self._hierarchy_cache = {}
            with open(self.local_file, encoding='utf-8') as afile:
                data = afile.read().splitlines()
                for item in parse_data(data):
                    parent, child = item[0], item[1]
                    self._hierarchy_cache[child] = parent

    def _get_hierarchy_cache(self, geonames_id):
        """ Given a geoname ID of a child, it returns a goename ID of parent from cache """

        if hasattr(self, '_hierarchy_cache'):
            try:
                return self._hierarchy_cache[geonames_id]
            except:
                pass
        return None


    def _get_parent_city(self, lat, lng, country_code, city_pop_min=50000):
        """ Get a parent city for a district """

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



