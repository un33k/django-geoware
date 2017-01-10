import os
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.db import transaction
from django.utils.encoding import smart_str

from ..base import GeoBaseCommand
from ...utils.common import *
from ...utils.updater import *
from ...utils.fetcher import *
from ...utils.fixer import *
from ...models import (Timezone, Country)

logger = logging.getLogger("geoware.cmd.timezone")

class Command(GeoBaseCommand):
    cmd_name = "timezone"

    def is_entry_valid(self, item):
        """
        Checks for minimum time zone requirements.
        """
        try:
            country_code = item[0]
            if len(country_code) != 2:
                return False
            name = item[1]
            gmt = item[2]
            dst = item[3]
        except:
            logger.warning("Invalid Record: ({item})".format(item=item))
            return False
        return True

    def get_query_kwargs(self, data):
        country = self._get_country_cache(data['country_code'])
        if country:
            return {'name_id': data['name_id'], 'country': country}
        return {}

    def record_to_dict(self, item):
        """
        Given a timezone record, it returns a dictionary.
        """
        dicts = {}
        try:
            dicts = {
                'country_code'  : get_str(item, 0),
                'name_id'       : get_str(item, 1),
                'gmt_offset'    : get_str(item, 2),
                'dst_offset'    : get_str(item, 3),
                'raw_offset'    : get_str(item, 4),
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

        timezone, created = self.get_geo_object(Timezone, data)
        if not created and not self.overwrite:
            return

        logger.debug("\n****************>>>\n{item}".format(item=item))

        timezone.gmt_offset = data.get('gmt_offset', timezone.gmt_offset)
        timezone.dst_offset = data.get('dst_offset', timezone.dst_offset)
        timezone.raw_offset = data.get('raw_offset', timezone.raw_offset)

        if data.get('country_code'):
            country = self._get_country_cache(data['country_code'])
            if country:
                timezone.country = country

        timezone.save()
