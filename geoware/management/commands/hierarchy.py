import os
import logging

from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ..base import GeoBaseCommand
from ...models import City
from ...utils.common import *
from ... import defaults as defs

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
        cities = City.objects.filter(geoname_id__in=[parent_id, child_id])
        if len(cities) != 2:
            return

        parent, child = [None, None]
        for city in cities:
            if city.geoname_id == parent_id:
                parent = city
            elif city.geoname_id == child_id:
                child = city

        if parent and child:
            parent.district_of = None
            parent.save()
            child.district_of = parent
            child.save()

            logger.debug("Updated Hierarchy: {item}".format(item=item))
