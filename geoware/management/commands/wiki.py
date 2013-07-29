import os
import sys
import logging
import resource
import progressbar
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.core.management import call_command
from django.db import transaction, reset_queries, IntegrityError
from django.db.models import Q

from toolware.utils.query import get_null_or_blank_query
from toolware.utils.query import get_not_null_and_not_blank_query

from wikiware.wiki import get_wiki_summary

from ... import defaults
from ...models import (Ocean, Continent, Country, Region, Subregion,
    City, District, Language, Currency, Timezone)

logger = logging.getLogger("geoware.cmd.wiki")

class Command(BaseCommand):
    cmd_name = 'Wiki'
    help = """usage: %prog <[-t SEARCH_TYPES] | [--all]>[-n SEARCH_NAMES][--overwrite]
    \nThis command fetches related location info from Wikipedia
    """
    available_types = [
        ['Ocean', Ocean],
        ['Continent', Continent],
        ['Country', Country],
        ['Region', Region],
        ['Subregion', Subregion],
        ['City', City],
        ['District', District],
    ]

    def _progress_widget(self, name):
        class MemoryUsageWidget(progressbar.ProgressBarWidget):
            def update(self, pbar):
                return '{0} kB'.format(str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss).rjust(8))

        widgets = [
            '{0}|RAM usage:'.format("Wiki |Fetching:  {0}".format((name[:10] + (name[10:] and '..')).rjust(10))),
            MemoryUsageWidget(),
            '|',
            progressbar.ETA(),
            '|Done:',
            progressbar.Percentage(),
            progressbar.Bar(),
        ]
        return widgets

    option_list = BaseCommand.option_list + (
        make_option('-o', '--overwrite', action='store_true', default=False,
            help='Overwrite any locally modified data with the new fetched data.'
        ),
        make_option('-t', action='append', dest='search_types', default=[],
            help='Search and update by object type. Example: wiki -t country. Available types: {}'.format(
                 ', '.join([x[0].lower() for x in available_types])),
        ),
        make_option('-n', action='append', dest='search_names', default=[],
            help='Search and update by name. Example: wiki -t city -n Ottawa -n Waterloo'
        ),
        make_option('-a', '--all', action='store_true', default=False,
            help='Search and update all object types.'
        ),
    )

    def handle(self, *args, **options):
        self.options = options
        self.all = self.options['all']
        self.overwrite = self.options['overwrite']
        self.search_types = self.options['search_types']
        self.search_names = self.options['search_names']

        if not self.all and not self.search_types:
            self.print_help("", subcommand=self.cmd_name.lower())
            return
        if self.all and self.search_types:
            self.print_help("", subcommand=self.cmd_name.lower())
            return

        search_types_list = []
        if self.all:
            search_types_list = self.available_types
        else:
            for a in self.search_types:
                for b in self.available_types:
                    if a.lower() == b[0].lower():
                        search_types_list.append(b)

        for stype in search_types_list:
            self.fetch_info_for_type(stype)

    def fetch_info_for_type(self, search_type):
        name_q = Q()
        for name in self.search_names:
            name_q |= Q(**{"name__iexact": name})

        search_name, search_klass = search_type
        if self.overwrite:
            items = search_klass.objects.filter(is_active=True).filter(name_q).order_by('name')
            total_rows = search_klass.objects.filter(is_active=True).filter(name_q).count()
        else:
            query_url = get_not_null_and_not_blank_query('url')
            query_info = get_null_or_blank_query('info')
            items = search_klass.objects.filter(is_active=True).filter(query_url).filter(query_info).filter(name_q).order_by('name')
            total_rows = search_klass.objects.filter(is_active=True).filter(query_url).filter(query_info).filter(name_q).count()

        loop_counter = 0
        row_count = 0
        progress = progressbar.ProgressBar(maxval=total_rows, widgets=self._progress_widget(search_name))
        for item in items:
            row_count += 1; progress.update(row_count)
            try:
                item.info = self.fetch_wikipedia_summary(item)
            except:
                logger.error(_("Failed to fetch. ({0})\n").format(item.name))
                continue
            else:
                logger.debug(_("Fetched. ({0})\n").format(item.name))
            item.save()
            if loop_counter == 500:
                loop_counter = 0
                reset_queries()
            loop_counter = loop_counter + 1

    def fetch_wikipedia_summary(self, obj):
        summary = ''
        if obj.url and 'wikipedia' in obj.url:
            title = obj.url.split('/')[-1]
            summary = get_wiki_summary(title=title)
        if not summary:
            summary = get_wiki_summary(title=obj.name)
        # print summary + "\n"
        return summary.strip()



