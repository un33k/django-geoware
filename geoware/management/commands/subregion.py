import os
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.utils.encoding import smart_str

from ..base import GeoBaseCommand
from ...utils.updater import *
from ...utils.fetcher import *
from ...utils.fixer import *
from ...models import (Subregion, Region, Country)

logger = logging.getLogger("geoware.cmd.subregion")

class Command(GeoBaseCommand):
    cmd_name = "Subregion"

    def is_entry_valid(self, item):
        try:
            fips = item[0]
            name = item[2]
            geoid = int(item[3])
        except:
            return False
        return True

    def get_query_kwargs(self, data):
        region = self._get_region_cache(data['region_fips'])
        if region:
            return {'name': data['name'], 'region': region}
        return {}

    def save_or_update_entry(self, item):
        """ Save or update a given entry into DB """

        data = self.entry_to_dict(item)
        if not data:
            return

        subregion = self.get_geo_object(Subregion, data)
        if not subregion:
            return

        logger.debug("\n****************>>>\n{0}".format(item))

        subregion.geoname_id = data['geoid']
        if (not subregion.code) or self.overwrite: subregion.code = data['code']
        if (not subregion.name) or self.overwrite: subregion.name = data['name']
        if (not subregion.name_std) or self.overwrite: subregion.name_std = data['name_std']
        if (not subregion.fips) or self.overwrite: subregion.fips = data['fips']

        if data['region_fips']:
            subregion.region = self._get_region_cache(data['region_fips'])
        if not subregion.region:
            return
        
        subregion_pre_save_call(subregion)

        success, reason = self.save_to_db(subregion)
        if success:
            logger.debug("Added {0}: {1} ({2})".format(self.cmd_name, subregion, subregion.fips))
        else:
            logger.error("Failed to add {0}: {1} ({2}) [{3}]".format(self.cmd_name, subregion, subregion.fips, reason))

    def entry_to_dict(self, item):
        """ Given a list of info for an entry, it returns a dict """

        get_field = lambda x,i: x[i] if len(x)>i else ''
        try:
            item = [force_unicode(x) for x in item]
        except:
            pass
        dicts = {}
        try:
            dicts = {
                'region_fips'       : '.'.join(get_field(item, 0).split('.')[:2]),
                'code'              : get_field(item, 0).split('.')[2],
                'fips'              : get_field(item, 0),
                'name_std'          : smart_str(get_field(item, 1)),
                'name'              : smart_str(get_field(item, 2)),
                'geoid'             : get_field(item, 3),
            }
        except Exception, e:
            logger.warning("Failed to extract {0} data. {1}".format(self.cmd_name, item))
        return dicts






