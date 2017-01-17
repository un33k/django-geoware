import os
import logging

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ...models import Country
from ...models import Division
from ...models import Subdivision

from ..utils.base import GeoBaseCommand
from ..utils.common import *
from ..utils.handler import *

logger = logging.getLogger("geoware.cmd.subdivision")


class Command(GeoBaseCommand):
    cmd_name = "subdivision"

    def is_entry_valid(self, item):
        """
        Checks for minimum subdivision requirements.
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
        Fields to identify a subdivision record.
        """
        division = self._get_division_cache(data['division_fips'])
        if division:
            return {'fips': data['fips'], 'name_std': data['name_std'], 'division': division}
        return {}

    def record_to_dict(self, item):
        """
        Given a division record, it returns a dictionary.
        """
        data = {}
        try:
            data = {
                'division_fips' : '.'.join(get_str(item, 0).split('.')[:2]),
                'code'          : get_str(item, 0).split('.')[2],
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

        if data.get('division_fips'):
            division = self._get_division_cache(data['division_fips'])
            if not division:
                return

        subdivision, created = self.get_geo_object(Subdivision, data)
        if not subdivision or (not created and not self.overwrite):
            return

        logger.debug("{action} Subdivision: {item}".format(action="Added" if created else "Updated", item=item))

        subdivision.geoname_id = data.get('geoid')
        subdivision.code = data.get('code', subdivision.code)
        subdivision.name = data.get('name', subdivision.name)
        subdivision.fips = data.get('fips', subdivision.fips)
        subdivision.name_std = data.get('name_std', division.name_std)
        subdivision.division = division

        subdivision_custom_handler(subdivision)
        subdivision.save()
