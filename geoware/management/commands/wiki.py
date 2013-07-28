import os
import sys
import logging
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.core.management import call_command
from django.db.models import Q

from toolware.utils.query import get_null_or_blank_query
from toolware.utils.query import get_not_null_and_not_blank_query

from wikiware.wiki import get_wiki_summary

from ... import defaults
from ...models import (Ocean, Continent, Country, Region, Subregion,
    City, District, Language, Currency, Timezone)

logger = logging.getLogger("geoware.cmd.wikipedia")

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
        ['Language', Language],
        ['Currency', Currency],
        ['Timezone', Timezone],
    ]
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

        for klass in search_types_list:
            self.fetch_info_for_type(klass[1])
    
    def fetch_info_for_type(self, klass):
        name_q = Q()
        for name in self.search_names:
            name_q |= Q(**{"name__iexact": name})
        if self.overwrite:
            instances = klass.objects.filter(is_active=True).filter(name_q)
        else:
            query_url = get_not_null_and_not_blank_query('url')
            query_info = get_null_or_blank_query('info')
            instances = klass.objects.filter(is_active=True).filter(query_url).filter(query_info).filter(name_q)
        for instance in instances:
            info = self.fetch_wikipedia_summary(instance)
            instance.info = info
            instance.save()
    
    def fetch_wikipedia_summary(self, obj):
        summary = get_wiki_summary(title=obj.name)
        if not summary and 'wikipedia' in obj.url:
            title = obj.url.split('/')[-1]
            summary = get_wiki_summary(title=title)
        print summary, "\n"
        return summary.strip()



