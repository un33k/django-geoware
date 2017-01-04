import os
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
from ...models import (Timezone, Country)

logger = logging.getLogger("geoware.cmd.timezone")

class Command(GeoBaseCommand):
    cmd_name = "Timezone"

    def is_entry_valid(self, item):
        try:
            country_code = item[0]
            if len(country_code) != 2:
                return False
            name = item[1]
            gmt = item[2]
            dst = item[3]
        except:
            return False
        return True


    def get_query_kwargs(self, data):
        country = self._get_country_cache(data['country_code'])
        if country:
            return {'name_id': data['name_id'], 'country': country}
        return {}


    def save_or_update_entry(self, item):
        """ Save or update a given entry into DB """

        data = self.entry_to_dict(item)
        if not data:
            return

        timezone = self.get_geo_object(Timezone, data)
        if not timezone:
            return

        logger.debug("\n****************>>>\n{0}".format(item))

        if (not timezone.name_id) or self.overwrite: timezone.name_id = data['name_id']
        if (not timezone.gmt_offset) or self.overwrite: timezone.gmt_offset = data['gmt_offset']
        if (not timezone.dst_offset) or self.overwrite: timezone.dst_offset = data['dst_offset']
        if (not timezone.raw_offset) or self.overwrite: timezone.raw_offset = data['raw_offset']

        if data['country_code']:
            country = self._get_country_cache(data['country_code'])
            if country:
                timezone.country = country

        fix_timezone_pre_save(timezone)

        success, reason = self.save_to_db(timezone)
        if success:
            logger.debug("Added {0}: {1} ({2})".format(self.cmd_name, timezone, timezone.country))
        else:
            logger.error("Failed to add {0}: {1} ({2}) [{3}]".format(self.cmd_name, timezone, timezone.country, reason))


    def entry_to_dict(self, item):
        """ Given a list of info for an entry, it returns a dict """

        get_field = lambda x,i: x[i] if len(x)>i else ''
        try:
            item = [smart_str(x) for x in item]
        except:
            pass
        dicts = {}
        try:
            dicts = {
                'country_code'      : get_field(item, 0),
                'name_id'           : smart_str(get_field(item, 1)),
                'gmt_offset'        : get_field(item, 2),
                'dst_offset'        : get_field(item, 3),
                'raw_offset'        : get_field(item, 4),
            }
        except Exception as e:
            logger.warning("Failed to extract {0} data. {1}".format(self.cmd_name, item))
        return dicts


