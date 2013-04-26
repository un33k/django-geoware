import os
import sys
import logging
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.core.management import call_command

from ... import defaults

logger = logging.getLogger("geoware.cmd.geo")

class Command(BaseCommand):
 
    help = "usage: %prog <--download> | <--load> [--force][--memory][--speed][--overwrite] \n\tThis command loads all geoname data into your database"

    option_list = BaseCommand.option_list + (
        make_option('-d', '--download', action='store_true', default=False,
            help='Download the related files if newer files are available.'
        ),
        make_option('-l', '--load', action='store_true', default=False,
            help='Load the info from the downloaded files into the DB'
        ),
        make_option('-f', '--force', action='store_true', default=False,
            help='Force an action.'
        ),
        make_option('-m', '--memory', action='store_true', default=True,
            help='Optimize for systems with lower system memory. (default)'
        ),
        make_option('-s', '--speed', action='store_true', default=False,
            help='Optimize for systems with higher system memory.'
        ),
        make_option('-o', '--overwrite', action='store_true', default=False,
            help='Overwrite any locally modified data with the new dowloaded data.'
        ),
    )

    def handle(self, *args, **options):
        if not options['download'] and not options['load']:
            self.print_help("", subcommand='geo')
            return

        for cmd in defaults.GEOWARE_LOADING_ORDER:
            call_command(cmd.lower(), **options)





