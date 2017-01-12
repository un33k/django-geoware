import os
import logging

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ...models import Country
from ...models import Region
from ...models import Subregion
from ...models import City
from ...models import Altname

from ..utils.base import GeoBaseCommand
from ..utils.common import *
from ..utils.handler import *

logger = logging.getLogger("geoware.cmd.altname")


class Command(GeoBaseCommand):
    cmd_name = "altname"

    def is_altname_link(self, code, name):
        if code.strip().lower() == 'link' or any(p in name for p in ['http', 'wikipedia', '//']):
            return True
        return False

    def is_entry_valid(self, item):
        """
        Checks for minimum altname requirements.
        """
        is_valid = True
        try:
            alt_geoid = int(item[0])
            ref_geoid = int(item[1])
            code = item[2].strip()
            name_or_link = item[3]
        except:
            is_valid = False

        if is_valid and alt_geoid and ref_geoid and code and name_or_link:
            if self._get_language_cache(code) or self.is_altname_link(code, name_or_link):
                return is_valid

        logger.warning("Invalid Record: ({item})".format(item=item))
        return False

    def get_query_fields(self, data):
        """
        Fields to identify a alt record.
        """
        return {'geoname_id': data['geoid'], 'ref_geoname_id': data['ref_geoid']}

    def record_to_dict(self, item):
        """
        Given a altname record, it returns a dictionary.
        """
        data = {}
        try:
            data = {
                'geoid'             : get_str(item, 0),
                'ref_geoid'         : get_str(item, 1),
                'code'              : get_str(item, 2),
                'name'              : get_str(item, 3),
                'link'              : get_str(item, 3),
                'preferred'         : get_str(item, 4),
                'short'             : get_str(item, 5),
            }
        except Exception as err:
            logger.warning("Failed to extract {cmd} data. {record} {err}".format(cmd=self.cmd_name, record=item, err=err))
        return data

    def create_or_update_record(self, item):
        """ Save or update a given entry into DB """

        data = self.record_to_dict(item)
        if not data:
            return

        ref_obj = self._get_generic_entry_cache(data['ref_geoid'])
        if not ref_obj:
            return

        altname, created = self.get_geo_object(Altname, data)
        if not altname or (not created and not self.overwrite):
            return

        logger.debug("{action} Altname: {item}".format(action="Added" if created else "Updated", item=item))

        altname.language = data.get('language', altname.language)
        altname.name = data.get('name', altname.name)
        altname.is_preferred = data.get('preferred', altname.is_preferred)
        altname.is_short = data.get('short', altname.is_short)

        if data.get('country_code'):
            country = self._get_country_cache(data['country_code'])
            if country:
                region.country = country

        altname_custom_handler(altname)
        altname.save()

    def post_download_handler(self):
        """
        Load into the cache anything that has a geoname_id.
        """
        if not hasattr(self, '_generic_entries_cache'):
            self._generic_entries_cache = {}
            for klass in (City, Subregion, Region, Country):
                for entry in klass.objects.all():
                    self._generic_entries_cache[entry.geoname_id] = entry

    def _get_generic_entry_cache(self, geoname_id):
        if not hasattr(self, '_generic_entries_cache'):
            self.post_download_handler()
        try:
            return self._generic_entries_cache[geoname_id]
        except KeyError:
            return None





