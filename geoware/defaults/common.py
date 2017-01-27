import os

from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.exceptions import ImproperlyConfigured

GEOWARE_COORDINATES_FORMAT = ('lng', 'lng',)

GEOWARE_USING_GIS = getattr(settings, 'GEOWARE_USING_GIS', False)
if GEOWARE_USING_GIS:
    GEOWARE_COORDINATES_FORMAT = ('point',)
    MIGRATION_MODULES = getattr(settings, 'MIGRATION_MODULES', {})
    if not MIGRATION_MODULES.get('geoware'):
        raise ImproperlyConfigured("""GEOWARE_USING_GIS is True, however, \n
            geoware is not configured in MIGRATION_MODULES""")

GEOWARE_DATA_DIR = getattr(settings, 'GEOWARE_DATA_DIR',
    os.path.abspath(os.path.join(os.path.expanduser("~"), '.geoware')))

GEOWARE_BASE_URLS = {
    'geonames': {
        'dump': 'http://download.geonames.org/export/dump/',
        'zip': 'http://download.geonames.org/export/zip/',
    },
}

GEOWARE_CITY_FILE_POPULATION_MIN = getattr(settings, 'GEOWARE_CITY_FILE_POPULATION_MIN', 1000)
if GEOWARE_CITY_FILE_POPULATION_MIN not in [1000, 5000, 15000]:
    GEOWARE_CITY_FILE_POPULATION_MIN = 15000

GEOWARE_FILE_DICT = {
    'country': {
        'remote': 'countryInfo.txt',
        'local': 'countryInfo.txt',
        'url': GEOWARE_BASE_URLS['geonames']['dump'] + '{filename}',
    },
    'division': {
        'remote': 'admin1CodesASCII.txt',
        'local': 'admin1CodesASCII.txt',
        'url': GEOWARE_BASE_URLS['geonames']['dump'] + '{filename}',
    },
    'subdivision': {
        'remote': 'admin2Codes.txt',
        'local': 'admin2Codes.txt',
        'url': GEOWARE_BASE_URLS['geonames']['dump'] + '{filename}',
    },
    'city': {
        'remote': 'cities{population}.zip'.format(population=GEOWARE_CITY_FILE_POPULATION_MIN),
        'local': 'cities{population}.txt'.format(population=GEOWARE_CITY_FILE_POPULATION_MIN),
        'url': GEOWARE_BASE_URLS['geonames']['dump'] + '{filename}',
    },
    'timezone': {
        'remote': 'timeZones.txt',
        'local': 'timeZones.txt',
        'url': GEOWARE_BASE_URLS['geonames']['dump'] + '{filename}',
    },
    'hierarchy': {
        'remote': 'hierarchy.zip',
        'local': 'hierarchy.txt',
        'url': GEOWARE_BASE_URLS['geonames']['dump'] + '{filename}',
    },
    'altname': {
        'remote': 'alternateNames.zip',
        'local': 'alternateNames.txt',
        'url': GEOWARE_BASE_URLS['geonames']['dump'] + '{filename}',
    },
    'language': {
        'remote': 'alternateNames.zip',
        'local': 'iso-languagecodes.txt',
        'url': GEOWARE_BASE_URLS['geonames']['dump'] + '{filename}',
    },
    'postalcode': {
        'remote': 'allCountries.zip',
        'local': 'allCountries.txt',
        'url': GEOWARE_BASE_URLS['geonames']['zip'] + '{filename}',
    },
}

GEOWARE_LOADING_ORDER = [
    'Country',
    'Timezone',
    'Division',
    'Subdivision',
    'City',
    'Altname',
]
