import os
import sys
import logging
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.core.management import call_command

from toolware.utils.query import get_null_or_blank_query
from toolware.utils.query import get_not_null_and_not_blank_query

from wikiware.wiki import get_wiki_summary

from ... import defaults
from ...models import Country

logger = logging.getLogger("geoware.cmd.wikipedia")

class Command(BaseCommand):
 
    help = "usage: %prog [--retry][--overwrite] \n\tThis command fetches related location info from Wikipedia"

    option_list = BaseCommand.option_list + (
        make_option('-o', '--overwrite', action='store_true', default=False,
            help='Overwrite any locally modified data with the new fetched data.'
        ),
    )

    def handle(self, *args, **options):
        self.options = options
        self.overwrite = self.options['overwrite']
        self.fetch_country()
    
    def fetch_country(self):
        if self.overwrite:
            countries = Country.objects.filter(is_active=True)
        else:
            query_url = get_not_null_and_not_blank_query('url')
            query_info = get_null_or_blank_query('info')
            countries = Country.objects.filter(is_active=True).filter(query_url).filter(query_info)
        for country in countries:
            info = self.fetch_wikipedia_paragraph(country)
            country.info = info
            country.save()
    
    def fetch_wikipedia_paragraph(self, obj):
        summary = get_wiki_summary(title=obj.name)
        if not summary and 'wikipedia' in obj.url:
            title = obj.url.split('/')[-1]
            summary = get_wiki_summary(title=title)
        print summary, "\n"
        return summary.strip()



