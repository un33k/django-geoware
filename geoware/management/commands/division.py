import os
import logging

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ...models import Country
from ...models import Division

from ..utils.base import GeoBaseCommand
from ..utils.common import *
from ..utils.handler import *

logger = logging.getLogger("geoware.cmd.division")


class Command(GeoBaseCommand):
    cmd_name = "division"

    def is_entry_valid(self, item):
        """
        Checks for minimum division requirements.
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
        Fields to identify a division record.
        """
        country = self._get_country_cache(data['country_code'])
        if country:
            return {'fips': data['fips'], 'name_std': data['name_std'], 'country': country}
        return {}

    def record_to_dict(self, item):
        """
        Given a division record, it returns a dictionary.
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

        division, created = self.get_geo_object(Division, data)
        if not division or (not created and not self.overwrite):
            return

        logger.debug("{action} Division: {item}".format(action="Added" if created else "Updated", item=item))

        division.geoname_id = data.get('geoid')
        division.code = data.get('code', division.code)
        division.name = data.get('name', division.name)
        division.fips = data.get('fips', division.fips)
        division.name_std = data.get('name_std', division.name_std)

        if data.get('country_code'):
            country = self._get_country_cache(data['country_code'])
            if country:
                division.country = country

        division_custom_handler(division)
        division.save()
