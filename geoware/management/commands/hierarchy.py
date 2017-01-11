import os
import logging

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ...models import City

from ..utils.base import GeoBaseCommand
from ..utils.common import *
from ..utils.handler import *

logger = logging.getLogger("geoware.cmd.hierarchy")


class Command(GeoBaseCommand):
    cmd_name = "hierarchy"

    def is_entry_valid(self, item):
        """
        Checks for minimum hierarchy requirements.
        """
        is_valid = True
        try:
            parent = int(item[0])
            child = int(item[1])
        except:
            is_valid = False

        if is_valid and parent and child:
            return is_valid

        logger.warning("Invalid Record: ({item})".format(item=item))
        return False

    def create_or_update_record(self, item):
        """
        Update parent, child hierarchy for district & city.
        """
        parent_id, child_id = [get_int(item, 0), get_int(item, 1)]
        parent, child = self._get_city_hierarchy_cache(parent_id, child_id)
        if parent and child:
            child.district_of = parent
            child.save()
            logger.debug("Updated Hierarchy: {item}".format(item=item))
