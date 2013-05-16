import os
import sys
import logging
import resource
import progressbar
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.db import transaction, reset_queries, IntegrityError

from ...models import *
from ... import defaults

logger = logging.getLogger("geoware.cmd.finalize")

class Command(BaseCommand):
 
    help = "usage: %prog <--absolute_url> [--overwrite] [--speed]"
    cmd_name = 'finish'
    absolute_url_object_list = [
        ['Ocean', Ocean],
        ['Continent', Continent],
        ['Country', Country],
        ['Region', Region],
        ['Subregion', Subregion],
        ['City', City],
        ['District', District],
    ]

    option_list = BaseCommand.option_list + (
        make_option('-u', '--absolute_url', action='store_true', default=False,
            help='Prebuild absolute URL from hierarchy.'
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

    def init_progressbar(self, action, name):
        class MemoryUsageWidget(progressbar.ProgressBarWidget):
            def update(self, pbar):
                return '{0} kB'.format(str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss).rjust(8))

        self.widgets = [
            '{0}|RAM usage:'.format("|{0}:  {1}".format(action, (name[:10] + (name[10:] and '..')).rjust(13))),
            MemoryUsageWidget(),
            '|',
            progressbar.ETA(),
            '|Done:',
            progressbar.Percentage(),
            progressbar.Bar(),
        ]
    
    def handle(self, *args, **options):
        self.options = options
        self.absolute_url = self.options['absolute_url']
        self.overwrite = self.options['overwrite']
        self.speed = self.options['speed']

        if self.absolute_url:
            self.finalize_absolute_url()
            return

        self.print_help("", subcommand=self.cmd_name.lower())

    def finalize_absolute_url(self):
        for klass in self.absolute_url_object_list:
            self.finish(klass[0], klass[1])

    def finish(self, name, klass):
        total_rows = klass.objects.all().count()
        if not total_rows:
            return
        self.init_progressbar("Abs URL", name)
        data = klass.objects.all()
        if self.speed:
            data = list(data)

        loop_counter = 0
        row_count = 0
        progress = progressbar.ProgressBar(maxval=total_rows, widgets=self.widgets)
        for instance in data:
            row_count += 1; progress.update(row_count)
            self.build_absolute_url(instance)
            if loop_counter == 500:
                loop_counter = 0
                reset_queries()
            loop_counter = loop_counter + 1

    def build_absolute_url(self, instance):
        if hasattr(instance, 'build_absolute_url'):
            instance.build_absolute_url(overwrite=self.overwrite)





