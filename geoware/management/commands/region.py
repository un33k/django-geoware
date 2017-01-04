import os
import logging
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ..base import GeoBaseCommand
from ...utils.updater import *
from ...utils.fetcher import *
from ...utils.fixer import *
from ...models import (Region, Country)

logger = logging.getLogger("geoware.cmd.region")

class Command(GeoBaseCommand):
    cmd_name = "Region"

    def is_entry_valid(self, item):
        try:
            fips = item[0]
            name = item[2]
            geoid = int(item[3])
        except:
            return False
        return True


    def get_query_kwargs(self, data):
        country = self._get_country_cache(data['country_code'])
        if country:
            return {'name': data['name'], 'country': country}
        return {}

    def save_or_update_entry(self, item):
        """ Save or update a given entry into DB """

        data = self.entry_to_dict(item)
        if not data:
            return

        region = self.get_geo_object(Region, data)
        if not region:
            return

        logger.debug("\n****************>>>\n{0}".format(item))

        region.geoname_id = data['geoid']
        if (not region.code) or self.overwrite: region.code = data['code']
        if (not region.name) or self.overwrite: region.name = data['name']
        if (not region.name_std) or self.overwrite: region.name_std = data['name_std']
        if (not region.fips) or self.overwrite: region.fips = data['fips']

        if data['country_code']:
            region.country = self._get_country_cache(data['country_code'])
        if not region.country:
            return

        region_pre_save_call(region)

        success, reason = self.save_to_db(region)
        if success:
            logger.debug("Added {0}: {1} ({2})".format(self.cmd_name, region, region.fips))
        else:
            logger.error("Failed to add {0}: {1} ({2}) [{3}]".format(self.cmd_name, region, region.fips, reason))


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
                'country_code'      : get_field(item, 0).split('.')[0],
                'code'              : get_field(item, 0).split('.')[1],
                'fips'              : get_field(item, 0),
                'name_std'          : smart_str(get_field(item, 1)),
                'name'              : smart_str(get_field(item, 2)),
                'geoid'             : get_field(item, 3),
            }
        except Exception as e:
            logger.warning("Failed to extract {0} data. {1}".format(self.cmd_name, item))
        return dicts






