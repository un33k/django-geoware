import os
import logging

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ...models import Country
from ...models import Region
from ...models import Subregion
from ...models import City

from ... import defaults as defs

from ..utils.base import GeoBaseCommand
from ..utils.common import *
from ..utils.handler import *

if defs.GEOWARE_USING_GIS:
    from django.contrib.gis.geos import Point

logger = logging.getLogger("geoware.cmd.city")


class Command(GeoBaseCommand):
    cmd_name = "city"

    def is_entry_valid(self, item):
        """
        Checks for minimum subregion requirements.
        """
        is_valid = True
        try:
            geoid = int(item[0])
            name = item[2]
            lat = item[4]
            lng = item[5]
            code = item[7]
            country_code = item[8]
        except:
            is_valid = False

        if is_valid and name and lat and lng and code and len(country_code) == 2:
            return is_valid

        logger.warning("Invalid Record: ({item})".format(item=item))
        return False

    def get_query_fields(self, data):
        """
        Fields to identify a city record.
        """
        fields = {'name': data['name']}
        country = self._get_country_cache(data['country_code'])
        if country:
            fields['country'] = country
            region = self._get_country_cache(data['region_code'])
            if region:
                fields['region'] = region
        return fields

    def record_to_dict(self, item):
        """
        Given a city record, it returns a dictionary.
        """
        data = {}
        try:
            data = {
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

        code = data.get('city_code')
        if not code or code in defs.GEOWARE_INVALID_CITY_TYPES:
            logger.warning("Invalid {code} {cmd} data. {record}".format(code=code, cmd=self.cmd_name, record=item))
            data = {}

        return data

    def create_or_update_record(self, item):
        """
        Create or update a given entry into DB
        """
        data = self.record_to_dict(item)
        if not data:
            return

        city, created = self.get_geo_object(City, data)
        if not city or (not created and not self.overwrite):
            return

        logger.debug("{action} City: {item}".format(action="Added" if created else "Updated", item=item))

        city.geoname_id = data.get('geoid')
        city.name = data.get('name', city.name)
        city.name_std = data.get('name_std', city.name_std)
        city.elevation = data.get('elevation', city.elevation)
        city.population = data.get('population', city.population)
        city.country = country

        if defs.GEOWARE_USING_GIS:
            city.point = Point(data['latitude'], data['longitude'])
        else:
            city.lat = data.get('lat', city.lat)
            city.lng = data.get('lng', city.lng)

        if data.get('region_code'):
            fips = '.'.join([data['country_code'], data['region_code']])
            region = self._get_region_cache(fips)
            if region:
                city.region = region

        if data.get('subregion_code'):
            fips = '.'.join([data['country_code'], data['region_code'], data['subregion_code']])
            subregion = self._get_region_cache(fips)
            if subregion:
                city.subregion = subregion

        if data.get('timezone'):
            timezone = self._get_timezone_cache(data['timezone'])
            if timezone:
                city.timezone = timezone

        city_custom_handler(city)
        city.save()

        if data['city_code'] in defs.GEOWARE_CAPITAL_TYPES:
            city.country.capital = city
            city.country.save()
