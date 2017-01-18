import os
import logging

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ...models import Country
from ...models import Division
from ...models import Subdivision
from ...models import City
from ...models import Altname

from ..utils.base import GeoBaseCommand
from ..utils.common import *
from ..utils.handler import *

logger = logging.getLogger("geoware.cmd.altname")


class Command(GeoBaseCommand):
    cmd_name = "altname"

    def is_altname_link(self, name_or_link):
        name_or_link = name_or_link.lower()
        if any(proto in name_or_link for proto in ['http', 'wikipedia', '//']):
            return True
        return False

    def is_entry_valid(self, item):
        """
        Checks for minimum altname requirements.
        """
        is_valid = True
        try:
            geoid = int(item[0])
            ref_geoid = int(item[1])
            code = item[2]
            name_or_link = item[3]
        except:
            is_valid = False

        if is_valid and geoid and ref_geoid and code and name_or_link:
            if self._get_language_cache(code):
                if not self.is_altname_link(name_or_link):
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

        altname.name = data.get('name', altname.name)
        altname.language = self._get_language_cache(data['code'])

        altname_custom_handler(altname)
        altname.save()
        ref_obj.altnames.add(altname)

    def post_download_handler(self):
        """
        Load into the cache anything that has a geoname_id.
        """
        if not hasattr(self, '_generic_entries_cache'):
            self._generic_entries_cache = {}
            for klass in (City, Subdivision, Division, Country):
                for entry in klass.objects.all():
                    self._generic_entries_cache[entry.geoname_id] = entry

    def _get_generic_entry_cache(self, geoname_id):
        if not hasattr(self, '_generic_entries_cache'):
            self.post_download_handler()
        try:
            return self._generic_entries_cache[geoname_id]
        except KeyError:
            return None
