import os
import logging

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ...models import Country
from ...models import Timezone

from ..utils.base import GeoBaseCommand
from ..utils.common import *
from ..utils.handler import *

logger = logging.getLogger("geoware.cmd.timezone")


class Command(GeoBaseCommand):
    cmd_name = "timezone"

    def is_entry_valid(self, item):
        """
        Checks for minimum timezone requirements.
        """
        is_valid = True
        try:
            country_code = item[0]
            name = item[1]
            gmt = item[2]
            dst = item[3]
        except:
            is_valid = False

        if is_valid and name and gmt and dst and len(country_code) == 2:
            return is_valid

        logger.warning("Invalid Record: ({item})".format(item=item))
        return False

    def get_query_fields(self, data):
        """
        Fields to identify a timezone record.
        """
        country = self._get_country_cache(data['country_code'])
        if country:
            return {'name_id': data['name_id'], 'country': country}
        return {}

    def record_to_dict(self, item):
        """
        Given a timezone record, it returns a dictionary.
        """
        data = {}
        try:
            data = {
                'country_code'  : get_str(item, 0),
                'name_id'       : get_str(item, 1),
                'gmt_offset'    : get_str(item, 2),
                'dst_offset'    : get_str(item, 3),
                'raw_offset'    : get_str(item, 4),
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

        timezone, created = self.get_geo_object(Timezone, data)
        if not timezone or (not created and not self.overwrite):
            return

        logger.debug("{action} Timezone: {item}".format(action="Added" if created else "Updated", item=item))

        timezone.gmt_offset = data.get('gmt_offset', timezone.gmt_offset)
        timezone.dst_offset = data.get('dst_offset', timezone.dst_offset)
        timezone.raw_offset = data.get('raw_offset', timezone.raw_offset)

        if data.get('country_code'):
            country = self._get_country_cache(data['country_code'])
            if country:
                timezone.country = country

        timezone_custom_handler(timezone)
        timezone.save()
