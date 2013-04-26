import os
import sys
import logging
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.core.management import call_command
from django.conf import settings

from ... utils.downloader import *
from ... import defaults

logger = logging.getLogger("geoware.cmd.geoip")

class Command(BaseCommand):
 
    help = "usage: %prog\n\tThis command downloads and installs MaxMind's GeoIP files in GEOIP_PATH."

    def handle(self, *args, **options):
        path = getattr(settings, 'GEOIP_PATH', '')
        if not path:
            sys.stderr.write(_("Unable to find GEOIP_PATH in your settings.\n"))
            return

        for db in defaults.GEOWARE_BASE_URLS['maxmind']:
            extracted_file = db
            url = defaults.GEOWARE_BASE_URLS['maxmind'][db]
            zipfile = os.path.join(defaults.GEOWARE_DATA_DIR, os.path.basename(defaults.GEOWARE_BASE_URLS['maxmind'][db]))
            dbfile = os.path.join(path, os.path.basename(extracted_file))
            cmd = 'wget -q {0} -O {1} && gunzip -qfc {1} > {2}'.format(url, zipfile, dbfile)
            os.system(cmd)





