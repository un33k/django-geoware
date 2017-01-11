import os
import logging

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ...models import Country
from ...models import Region

from ..utils.base import GeoBaseCommand
from ..utils.common import *
from ..utils.handler import *

logger = logging.getLogger("geoware.cmd.region")


class Command(GeoBaseCommand):
    cmd_name = "region"

    def is_entry_valid(self, item):
        """
        Checks for minimum region requirements.
        """
        is_valid = True
        try:
            fips = item[0]
            name = item[2]
            geoid = int(item[3])
        except:
            is_valid = False

        if is_valid and fips and name:
            return is_valid

        logger.warning("Invalid Record: ({item})".format(item=item))
        return False

    def get_query_fields(self, data):
        """
        Fields to identify a region record.
        """
        country = self._get_country_cache(data['country_code'])
        if country:
            return {'fips': data['fips'], 'name_std': data['name_std'], 'country': country}
        return {}

    def record_to_dict(self, item):
        """
        Given a region record, it returns a dictionary.
        """
        data = {}
        try:
            data = {
                'country_code'  : get_str(item, 0).split('.')[0],
                'code'          : get_str(item, 0).split('.')[1],
                'fips'          : get_str(item, 0),
                'name_std'      : get_str(item, 1),
                'name'          : get_str(item, 2),
                'geoid'         : get_str(item, 3),
            }
        except Exception as err:
            logger.warning("Failed to extract {cmd} data. {record} {err}".format(cmd=self.cmd_name, record=item, err=err))
        return data

    def create_or_update_record(self, item):
        """
        Create or update a given entry into DB
        """
        data = self.record_to_dict(item)
        if not data:
            return

        region, created = self.get_geo_object(Region, data)
        if not region or (not created and not self.overwrite):
            return

        logger.debug("{action} Region: {item}".format(action="Added" if created else "Updated", item=item))

        region.geoname_id = data.get('geoid')
        region.code = data.get('code', region.code)
        region.name = data.get('name', region.name)
        region.fips = data.get('fips', region.fips)
        region.name_std = data.get('name_std', region.name_std)

        if data.get('country_code'):
            country = self._get_country_cache(data['country_code'])
            if country:
                region.country = country

        region_custom_handler(region)
        region.save()
