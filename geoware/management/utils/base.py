import os
import sys
import logging
import progressbar

from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.db import transaction
from django.db import reset_queries
from django.db import IntegrityError

from ...models import *
from .common import *
from .downloader import *
from .loaders import *

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
            '-s',
            '--speed',
            action='store_true',
            default=False,
            help='Optimize for systems with no memory constrains.'
        )

        parser.add_argument(
            '-o',
            '--overwrite',
            action='store_true',
            default=False,
            help='Overwrite any locally modified data with the newly downloaded data.'
        ),

    def __init__(self, *args, **kwargs):
        self.dld = FileDownloader()
        self.dld.stage(self.cmd_name)

        load_continents()
        load_oceans()
        load_currencies()
        load_languages()

        self.widgets = [
            MemoryUsage(),
            progressbar.ETA(),
            ' |Processed: ',
            progressbar.Counter(),
            ' |Done: ',
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
        self.verbosity = self.options['verbosity']

        if not self.download and not self.load:
            self.print_help("", subcommand=self.cmd_name.lower())
            return

        self.stdout.write("\nProcessing {cmd} data...".format(cmd=self.cmd_name))

        if self.download:
            self.dld.download(options['force'])
            self.dld.extract()

        if self.load:
            self.save_records_to_db()

    def save_records_to_db(self):
        """
        Save records to the database.
        """
        if not os.path.isfile(self.dld.extracted_file_path):
            self.stdout.write("Unable to find {type} file. Download it first.".format(type=self.cmd_name))
            return

        self.stdout.write("Loading {type} data...\n".format(type=self.cmd_name))

        if self.speed:
            with open(self.dld.extracted_file_path, encoding='utf-8') as afile:
                data = afile.read().splitlines()
                total_rows = sum(1 for line in data if line and line.lstrip()[0] != '#')
        else:
            data = open(self.dld.extracted_file_path, encoding='utf-8')
            total_rows = sum(1 for line in open(self.dld.extracted_file_path,
                encoding='utf-8') if line and line.lstrip()[0] != '#')

        loop_counter = 0
        row_count = 0
        progress = progressbar.ProgressBar(maxval=total_rows, widgets=self.widgets)
        for item in parse_data(data):
            row_count += 1
            progress.update(row_count)
            try:
                if not self.is_entry_valid(item):
                    continue
                self.create_or_update_record(item)
            except Exception as err:
                logger.warning("Failed to process {cmd}. {record}".format(cmd=self.cmd_name, record=item))
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
        self.post_load_handler()
        self.stdout.write("\n")

    def get_geo_object(self, klass, data):
        """
        Get Geo object from database.
        """
        fields = self.get_query_fields(data)
        if not fields:
            return (None, False)

        try:
            with transaction.atomic():
                instance, created = klass.objects.get_or_create(**fields)
        except IntegrityError:
            try:
                instance, created = klass(**fields).save(), True
            except Exception as err:
                logger.warning("Unable to add {klass}: (fields={fields}) [err={err}]".format(
                    klass=klass, fields=fields, err=err))
                return (None, False)
        except Exception as err:
            logger.warning("Unable to create {klass}: (fields={fields}) [err={err}]".format(
                klass=klass, fields=fields, err=err))
            return (None, False)

        return (instance, created)

    def _get_continent_cache(self, code):
        """
        Gets continent obj from the cache or database.
        """
        continent = None
        if not hasattr(self, '_continent_cache'):
            self._continent_cache = {}
            if self.speed:
                entries = Continent.objects.all()
                for entry in entries:
                    self._continent_cache[entry.code] = entry

        try:
            continent = self._continent_cache[code]
        except KeyError:
            try:
                self._continent_cache[code] = Continent.objects.get(code=code)
                continent = self._continent_cache[code]
            except Continent.DoesNotExist:
                pass

        return continent

    def _get_country_cache(self, code):
        """
        Gets country obj from the cache or database.
        """
        country = None
        if not hasattr(self, '_country_cache'):
            self._country_cache = {}
            if self.speed:
                entries = Country.objects.all()
                for entry in entries:
                    self._country_cache[entry.code] = entry

        try:
            country = self._country_cache[code]
        except KeyError:
            try:
                self._country_cache[code] = Country.objects.get(code=code)
                country = self._country_cache[code]
            except Country.DoesNotExist:
                pass

        return country

    def _get_division_cache(self, fips):
        """
        Gets division obj from the cache or database.
        """
        division = None
        if not hasattr(self, '_division_cache'):
            self._division_cache = {}
            if self.speed:
                entries = Division.objects.all()
                for entry in entries:
                    self._division_cache[entry.fips] = entry
        try:
            division = self._division_cache[fips]
        except KeyError:
            try:
                self._division_cache[fips] = Division.objects.get(fips=fips)
                division = self._division_cache[fips]
            except Division.DoesNotExist:
                pass

        return division

    def _get_subdivision_cache(self, fips):
        """
        Gets subdivision obj from the cache or database.
        """
        subdivision = None
        if not hasattr(self, '_subdivision_cache'):
            self._subdivision_cache = {}
            if self.speed:
                entries = Subdivision.objects.all()
                for entry in entries:
                    self._subdivision_cache[entry.fips] = entry
        try:
            subdivision = self._subdivision_cache[fips]
        except KeyError:
            try:
                self._subdivision_cache[fips] = Subdivision.objects.get(fips=fips)
                subdivision = self._subdivision_cache[fips]
            except Subdivision.DoesNotExist:
                pass

        return subdivision

    def _get_city_cache(self, geoname_id):
        """
        Gets city obj from the cache or database.
        """
        city = None
        if not hasattr(self, '_city_cache'):
            self._city_cache = {}
            if self.speed:
                entries = City.objects.all()
                for entry in entries:
                    if entry.geoname_id:
                        self._city_cache[entry.geoname_id] = entry

        try:
            city = self._city_cache[geoname_id]
        except KeyError:
            try:
                self._city_cache[geoname_id] = City.objects.get(geoname_id=geoname_id)
                city = self._city_cache[geoname_id]
            except City.DoesNotExist:
                pass

        return city

    def _get_currency_cache(self, code):
        """
        Gets currency obj from the cache or database.
        """
        currency = None
        if not hasattr(self, '_currency_cache'):
            self._currency_cache = {}
            if self.speed:
                entries = Currency.objects.all()
                for entry in entries:
                    if entry.code:
                        self._currency_cache[entry.code] = entry
        try:
            currency = self._currency_cache[code]
        except KeyError:
            try:
                self._currency_cache[code] = Currency.objects.get(code=code)
                currency = self._currency_cache[code]
            except Currency.DoesNotExist:
                pass

        return currency

    def _get_language_cache(self, code):
        """
        Gets language obj from the cache or database.
        """
        language = None
        if not hasattr(self, '_language_cache'):
            self._language_cache = {}
            if self.speed:
                entries = Language.objects.all()
                for entry in entries:
                    if entry.code:
                        self._language_cache[entry.code] = entry

        try:
            language = self._language_cache[code]
        except KeyError:
            try:
                self._language_cache[code] = Language.objects.get(code=code)
                language = self._language_cache[code]
            except Language.DoesNotExist:
                pass

        return language

    def _get_timezone_cache(self, code):
        """
        Gets timezone obj from the cache or database.
        """
        timezone = None
        if not hasattr(self, '_timezone_cache'):
            self._timezone_cache = {}
            if self.speed:
                entries = Timezone.objects.all()
                for entry in entries:
                    if entry.name_id:
                        self._timezone_cache[entry.name_id] = entry

        try:
            timezone = self._timezone_cache[code]
        except KeyError:
            try:
                self._timezone_cache[code] = Timezone.objects.get(name_id=code)
                timezone = self._timezone_cache[code]
            except Timezone.DoesNotExist:
                pass

        return timezone

    def _get_city_hierarchy_cache(self, parent_geoname_id, child_geoname_id):
        """
        Given parent,child geoname ids, it returns both objects from cache or database.
        """
        parent = self._get_city_cache(parent_geoname_id)
        if parent:
            child = self._get_city_cache(child_geoname_id)
            if child:
                return (parent, child)
        return (None, None)

    def is_entry_valid(self, item):
        """
        Tells if a row (data) is valid.
        """
        return False

    def create_or_update_record(self, item):
        """
        Saves or updates an object that corresponds to a row (item).
        """
        pass

    def record_to_dict(self, item):
        """
        Given a row (data), it returns converts it to a digestible dictionary.
        """
        return {}

    def get_query_fields(self):
        """
        Returns query fields for object type.
        """
        return {}

    def post_download_handler(self):
        """
        Performs any `post` download and `pre` process operations.
        """
        pass

    def post_load_handler(self):
        """
        Performs any post loading and operations.
        """
        pass
