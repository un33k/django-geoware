import os
import sys
import logging
import resource
import progressbar
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.db import transaction, reset_queries, IntegrityError

from ..models import *
from ..utils.downloader import *
from ..utils.updater import *
from ..utils.importer import *
from .. import defaults

logger = logging.getLogger("geoware.cmd.base")

class GeoBaseCommand(BaseCommand):
 
    help = "usage: %prog <--download> | <--load> [--force]"
    updated = False
    cmd_name = 'base'

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

    def __init__(self, *args, **kwargs):
        self.rfile = ''
        import_continents()
        import_oceans()
        import_currencies()
        import_languages()

        class MemoryUsageWidget(progressbar.ProgressBarWidget):
            def update(self, pbar):
                return '{0} kB'.format(str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss).rjust(8))

        self.widgets = [
            '{0}|RAM usage:'.format("|Loading:  {0}".format((self.cmd_name[:10] + (self.cmd_name[10:] and '..')).rjust(12))),
            MemoryUsageWidget(),
            '|',
            progressbar.ETA(),
            '|Done:',
            progressbar.Percentage(),
            progressbar.Bar(),
        ]
        return super(GeoBaseCommand, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        self.options = options
        self.fetch = self.options['download']
        self.force = self.options['force']
        self.load = self.options['load']
        self.overwrite = self.options['overwrite']
        self.speed = self.options['speed']
        if self.speed:
            self._data_cache = ''

        if not self.fetch and not self.load:
            self.print_help("", subcommand=self.cmd_name.lower())
            return

        if self.fetch:
            if not self.file_exists or self.force:
                self.download(force=self.force)
                if self.updated:
                    logger.debug(_("Download is complete. ({0})\n").format(self.local_file))
            else:
                sys.stderr.write(_("{0} seems to be up2date. Use -f option to force a download. ({1})\n").format(self.cmd_name, self.local_file))

        if self.load:
            self.download()
            if self.updated or self.force:
                self.load_enteries() 
            else:
                sys.stderr.write(_("{0} seems to be up2date. Use -f option to force a load.\n".format(self.cmd_name)))
        return

    @property
    def remote_file(self):
        if not self.rfile:
            self.rfile = defaults.GEOWARE_FILE_DICT[self.cmd_name.lower()]['url'].format(filename=defaults.GEOWARE_FILE_DICT[self.cmd_name.lower()]['filename'])
        return self.rfile

    @property
    def local_file(self):
        self.lfile = os.path.join(defaults.GEOWARE_DATA_DIR, os.path.basename(self.remote_file.replace('.zip', '.txt')))
        return self.lfile

    @property
    def file_exists(self):
        return os.path.exists(self.local_file)

    def download(self, force=False):
        """ Download if the remote file is newer """

        self.updated = False
        success, fileinfo = file_download(url=self.remote_file, extract=True, force=force)
        if success:
            if fileinfo['updated']:
                self.updated = True
            self.post_download_call()
        return self.updated


    def load_enteries(self):
        """ Load enteries into in database """

        if not self.updated:
            self.download()
        if not self.updated and not self.force:
            logger.info(_("{0} files are up2date".format(self.cmd_name)))
            return

        logger.info(_("Loading {0} data".format(self.cmd_name)))

        if hasattr(self, '_data_cache'):
            data = open(self.local_file, 'rb').read().split('\n')
            total_rows = sum(1 for line in data if line and line.lstrip()[0] != '#')
        else:
            data = open(self.local_file, 'rb')
            total_rows = sum(1 for line in open(self.local_file, 'rb') if line and line.lstrip()[0] != '#')

        loop_counter = 0
        row_count = 0
        progress = progressbar.ProgressBar(maxval=total_rows, widgets=self.widgets)
        for item in parse_data(data):
            row_count += 1; progress.update(row_count)
            try:
                if not self.is_entry_valid(item):
                    continue
                self.save_or_update_entry(item)
            except (UnicodeDecodeError, UnicodeEncodeError), e:
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


    def save_or_update_entry(self, item):
        """ Save or update a given entry """
        pass


    def entry_to_dict(self, item):
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
        obj = None
        kwargs = self.get_query_kwargs(data)
        if kwargs:
            try:
                obj = klass.objects.get(**kwargs)
            except klass.DoesNotExist:
                obj = klass(**kwargs)
            except Exception, e:
                logger.error("Failed to add {0}: (kwargs={1}) [err={2}]".format(klass.__class__.__name__, kwargs, e))
        return obj

    @transaction.commit_on_success
    def save_to_db(self, obj):
        """ Attemps to save an object to the database and rolls back if failed """
        success = True
        reason = ''
        try:
            obj.save()
        except IntegrityError, e:
            transaction.rollback()
            success = False
            reason = e
        except Exception, e:
            success = False
            reason = e

        return success, reason


    def _get_continent_cache(self, code):
        """ Gets continent objobj from the cache or database """

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



