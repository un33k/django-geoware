import os
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ..base import GeoBaseCommand
from ...utils.common import *
from ...utils.updater import *
from ...utils.fetcher import *
from ...utils.fixer import *
from ...models import (Subregion, Region, Country)

logger = logging.getLogger("geoware.cmd.subregion")


class Command(GeoBaseCommand):
    cmd_name = "subregion"

    def is_entry_valid(self, item):
        """
        Checks for minimum subregion requirements.
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
        Fields to identify a subregion record.
        """
        region = self._get_region_cache(data['region_fips'])
        if region:
            return {'fips': data['fips'], 'name_std': data['name_std'], 'region': region}
        return {}

    def record_to_dict(self, item):
        """
        Given a region record, it returns a dictionary.
        """
        dicts = {}
        try:
            dicts = {
                'region_fips'   : '.'.join(get_str(item, 0).split('.')[:2]),
                'code'          : get_str(item, 0).split('.')[2],
                'fips'          : get_str(item, 0),
                'name_std'      : get_str(item, 1),
                'name'          : get_str(item, 2),
                'geoid'         : get_str(item, 3),
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

        if data.get('region_fips'):
            region = self._get_region_cache(data['region_fips'])
            if not region:
                return

        subregion, created = self.get_geo_object(Subregion, data)
        if not subregion or (not created and not self.overwrite):
            return

        logger.debug("{action} Subregion: {item}".format(action="Added" if created else "Updated", item=item))

        subregion.geoname_id = data.get('geoid')
        subregion.code = data.get('code', subregion.code)
        subregion.name = data.get('name', subregion.name)
        subregion.fips = data.get('fips', subregion.fips)
        subregion.name_std = data.get('name_std', region.name_std)
        subregion.region = region

        subregion_pre_save_call(subregion)
        subregion.save()
