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
from ...models import (Altname, District, City, Subregion, Region, Country)

logger = logging.getLogger("geoware.cmd.altname")


class Command(GeoBaseCommand):
    cmd_name = "altname"

    def is_altname_link(self, code, name):
        has_link_pattern = lambda x: any(k in name for k in ['http', 'wikipedia', '//'])
        if code.strip().lower() == 'link' or has_link_pattern(name):
            return True
        return False

    def is_entry_valid(self, item):
        try:
            alt_geoid = item[0]
            entry_geoid = item[1]
            code = item[2].strip()
            name_or_link = item[3]
            if not self._get_language_cache(code):
                if not self.is_altname_link(code, name_or_link):
                    return False
        except:
            return False
        return True

    def get_query_kwargs(self, data):
        return {'geoname_id': data['geoid'], 'ref_geoname_id': data['entry_geoid']}

    def create_or_update_entry(self, item):
        """ Save or update a given entry into DB """

        data = self.record_to_dict(item)
        if not data:
            return

        entry = self._get_generic_entry_cache(data['entry_geoid'])
        if not entry:
            return

        altname = self.get_geo_object(Altname, data)
        if not altname:
            return

        logger.debug("\n****************>>>\n{0}".format(item))

        if ((not entry.url) or self.overwrite) and self.is_altname_link(data['code'], data['name']):
            if 'en.' in data['link']:
                entry.url = data['link'].strip('http://').strip('https://')
                entry.save()
                logger.debug("Added URL {0}: {1} ({2})".format(self.cmd_name, entry, entry.url))
            return

        if (not altname.language) or self.overwrite: altname.language = self._get_language_cache(data['code'])
        if (not altname.name) or self.overwrite: altname.name = data['name']
        if (not altname.is_preferred) or self.overwrite: altname.is_preferred = True if data['preferred'] else False
        if (not altname.is_short) or self.overwrite: altname.is_short = True if data['short'] else False

        fix_altname_pre_save(altname)

        success, reason = self.save_to_db(altname)
        if success:
            logger.debug("Added {0}: {1} ({2})".format(self.cmd_name, altname, entry))
            entry.altnames.add(altname)
        else:
            logger.error("Failed to add {0}: {1} ({2}) [{3}]".format(self.cmd_name, altname, entry, reason))


    def record_to_dict(self, item):
        """ Given a list of info for an entry, it returns a dict """

        get_field = lambda x,i: x[i] if len(x)>i else ''
        try:
            item = [smart_str(x) for x in item]
        except:
            pass
        dicts = {}
        try:
            dicts = {
                'geoid'             : get_field(item, 0),
                'entry_geoid'       : get_field(item, 1),
                'code'              : get_field(item, 2),
                'name'              : smart_str(get_field(item, 3)),
                'link'              : smart_str(get_field(item, 3)),
                'preferred'         : smart_str(get_field(item, 4)),
                'short'             : smart_str(get_field(item, 5)),
            }
        except Exception as e:
            logger.warning("Failed to extract {0} data. {1}".format(self.cmd_name, item))
        return dicts


    def post_download_call(self):
        """ Load into the cache anything that has a geoname_id """

        if not hasattr(self, '_generic_entries_cache'):
            self._generic_entries_cache = {}
            for klass in (District, City, Subregion, Region, Country):
                for entry in klass.objects.all():
                    self._generic_entries_cache[entry.geoname_id] = entry


    def _get_generic_entry_cache(self, geoname_id):
        if not hasattr(self, '_generic_entries_cache'):
            self.post_download_call()
        try:
            return self._generic_entries_cache[geoname_id]
        except:
            return None











