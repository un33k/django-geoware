import os
import sys
import logging
import resource
import progressbar

from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.db import transaction, reset_queries, IntegrityError

from ..models import *
from ..utils.common import *
from ..utils.downloader import *
from ..utils.updater import *
from ..utils.importer import *
from .. import defaults

logger = logging.getLogger("geoware.cmd.base")


class GeoBaseCommand(BaseCommand):
    """
    Base command for Geo related operations.
    """
    def add_arguments(self, parser):

        parser.add_argument(
            '-d',
            '--download',
            action='store_true',
            default=False,
            help='Download the related files if newer files are available.'
        )

        parser.add_argument(
            '-l',
            '--load',
            action='store_true',
            default=False,
            help='Load the info from the downloaded files into the DB'
        )
        parser.add_argument(
            '-f',
            '--force',
            action='store_true',
            default=False,
            help='Force an action.'
        )

        parser.add_argument(
            '-m',
            '--memory',
            action='store_true',
            default=False,
            help='Optimize for systems with lower system memory.'
        )

        parser.add_argument(
            '-s',
            '--speed',
            action='store_true',
            default=True,
            help='Optimize for systems with higher system memory. (default)'
        )

        parser.add_argument(
            '-o',
            '--overwrite',
            action='store_true',
            default=False,
            help='Overwrite any locally modified data with the newly downloaded data.'
        ),

    def __init__(self, *args, **kwargs):
        self._dld = FileDownloader()
        self._dld.stage(self.cmd_name)

        import_continents()
        import_oceans()
        import_currencies()
        import_languages()

        self._widgets = [
            progressbar.ETA(),
            '| Done: ',
            progressbar.Percentage(),
            progressbar.Bar(),
        ]
        return super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        self.options = options
        self.download = self.options['download']
        self.force = self.options['force']
        self.load = self.options['load']
        self.overwrite = self.options['overwrite']
        self.speed = self.options['speed']

        if not self.download and not self.load:
            self.print_help("", subcommand=self.cmd_name.lower())
            return

        if self.download:
            self._dld.download(options['force'])
            self._dld.extract()

        if self.load:
            self.save_records_to_db()

    def save_records_to_db(self):
        """
        Save records to the database.
        """
        self.stdout.write("Loading {type} data".format(type=self.cmd_name))

        if self.speed:
            with open(self._dld.extracted_file_path, encoding='utf-8') as afile:
                data = afile.read().splitlines()
                total_rows = sum(1 for line in data if line and line.lstrip()[0] != '#')
        else:
            data = open(self.extracted_file_name, encoding='utf-8')
            total_rows = sum(1 for line in open(self._dld.extracted_file_name, encoding='utf-8') if line and line.lstrip()[0] != '#')

        loop_counter = 0
        row_count = 0
        progress = progressbar.ProgressBar(maxval=total_rows, widgets=self.widgets)
        for item in parse_data(data):
            row_count += 1; progress.update(row_count)
            try:
                if not self.is_entry_valid(item):
                    continue
                self.create_or_update_entry(item)
            except (UnicodeDecodeError, UnicodeEncodeError) as e:
                continue
            if loop_counter == 500:
                loop_counter = 0
                reset_queries()
            loop_counter = loop_counter + 1

        try:
            data.close()
            del data
        except:
            pass
        self.post_load_call()

    def is_entry_valid(self, item):
        """ Tells if an item (row) is valid """
        return False


    def create_or_update_entry(self, item):
        """ Save or update a given entry """
        pass


    def record_to_dict(self, item):
        """ Given a list of info for an entry, it returns a dict """
        return {}


    def get_query_kwargs(self):
        """ Returns query keyword args for object """
        return {}


    def post_download_call(self):
        """ Performs any post download and pre process manipulations """
        pass

    def post_load_call(self):
        """ Performs any post loading and manipulations """
        pass

    def get_geo_object(self, klass, data):
        """
        Get Geo object from database.
        """
        kwargs = self.get_query_kwargs(data)
        try:
            obj, created = klass.objects.get_or_create(**kwargs)
        except klass.MultipleObjectsReturned:
            klass.objects.filter(**kwargs).delete()
            obj, created = klass.objects.get_or_create(**kwargs)
        return (obj, created)

    def _get_continent_cache(self, code):
        """ Gets continent obj from the cache or database """

        if not hasattr(self, '_continent_cache'):
            self._continent_cache = {}
            if self.speed:
                entries = Continent.objects.all()
                for entry in entries:
                    self._continent_cache[entry.code] = entry
        try:
            return self._continent_cache[code]
        except:
            try:
                self._continent_cache[code] = Continent.objects.get(code=code)
                return self._continent_cache[code]
            except:
                return None

    def _get_country_cache(self, code):
        """ Gets country obj from the cache or database """

        if not hasattr(self, '_country_cache'):
            self._country_cache = {}
            if self.speed:
                entries = Country.objects.all()
                for entry in entries:
                    self._country_cache[entry.code] = entry
        try:
            return self._country_cache[code]
        except:
            try:
                self._country_cache[code] = Country.objects.get(code=code)
                return self._country_cache[code]
            except:
                return None

    def _get_region_cache(self, fips):
        """ Gets region obj from the cache or database """

        if not hasattr(self, '_region_cache'):
            self._region_cache = {}
            if self.speed:
                entries = Region.objects.all()
                for entry in entries:
                    self._region_cache[entry.fips] = entry
        try:
            return self._region_cache[fips]
        except:
            try:
                self._region_cache[fips] = Region.objects.get(fips=fips)
                return self._region_cache[fips]
            except:
                return None

    def _get_subregion_cache(self, fips):
        """ Gets subregion obj from the cache or database """

        if not hasattr(self, '_subregion_cache'):
            self._subregion_cache = {}
            if self.speed:
                entries = Subregion.objects.all()
                for entry in entries:
                    self._subregion_cache[entry.fips] = entry
        try:
            return self._subregion_cache[fips]
        except:
            try:
                self._subregion_cache[fips] = Subregion.objects.get(fips=fips)
                return self._subregion_cache[fips]
            except:
                return None

    def _get_city_cache(self, geonames_id):
        """ Gets city obj from the cache or database """

        if not hasattr(self, '_city_cache'):
            self._city_cache = {}
            if self.speed:
                entries = City.objects.all()
                for entry in entries:
                    try:
                        self._city_cache[entry.geonames_id] = entry
                    except:
                        continue
        try:
            return self._city_cache[geonames_id]
        except:
            try:
                self._city_cache[geonames_id] = City.objects.get(geonames_id=geonames_id)
                return self._city_cache[geonames_id]
            except:
                return None

    def _get_hierarchy_cache(self, geonames_id):
        """ Given a geoname ID of a child, it returns a goename ID of parent from cache """

        return None

    def _get_currency_cache(self, code):
        """ Gets currency obj from the cache or database """

        if not hasattr(self, '_currency_cache'):
            self._currency_cache = {}
            if self.speed:
                entries = Currency.objects.all()
                for entry in entries:
                    try:
                        self._currency_cache[entry.code] = entry
                    except:
                        continue
        try:
            return self._currency_cache[code]
        except:
            try:
                self._currency_cache[code] = Currency.objects.get(code=code)
                return self._currency_cache[code]
            except:
                return None

    def _get_language_cache(self, code):
        """ Gets language obj from the cache or database """

        if not hasattr(self, '_language_cache'):
            self._language_cache = {}
            if self.speed:
                entries = Language.objects.all()
                for entry in entries:
                    try:
                        self._language_cache[entry.code] = entry
                    except:
                        continue
        try:
            return self._language_cache[code]
        except:
            try:
                self._language_cache[code] = Language.objects.get(code=code)
                return self._language_cache[code]
            except:
                return None

    def _get_timezone_cache(self, code):
        """ Gets timezone obj from the cache or database """

        if not hasattr(self, '_timezone_cache'):
            self._timezone_cache = {}
            if self.speed:
                entries = Timezone.objects.all()
                for entry in entries:
                    try:
                        self._timezone_cache[entry.name_id] = entry
                    except:
                        continue
        try:
            return self._timezone_cache[code]
        except:
            try:
                self._timezone_cache[code] = Timezone.objects.get(name_id=code)
                return self._timezone_cache[code]
            except:
                return None



