from django.utils.translation import ugettext as _

GEOWARE_GEONAME_CONTINENT_DATA = [
    {
        'code': 'AF',
        'iso_n': '002',
        'name': 'Africa',
        'geoname_id': '6255146'
    },
    {
        'code': 'AS',
        'iso_n': '149',
        'name': 'Asia',
        'geoname_id': '6255147'
    },
    {
        'code': 'EU',
        'iso_n': '150',
        'name': 'Europe',
        'geoname_id': '6255148'
    },
    {
        'code': 'NA',
        'iso_n': '021',
        'name': 'North America',
        'geoname_id': '6255149'
    },
    {
        'code': 'OC',
        'iso_n': '009',
        'name': 'Oceania',
        'geoname_id': '6255151'
    },
    {
        'code': 'SA',
        'iso_n': '005',
        'name': 'South America',
        'geoname_id': '6255150'
    },
    {
        'code': 'AN',
        'name': 'Antarctica',
        'geoname_id': '6255152'
    },
]

GEOWARE_CONTINENT_CHOICES = (
    ('AF', _('Africa')),
    ('AS', _('Asia')),
    ('EU', _('Europe')),
    ('OC', _('Oceania')),
    ('NA', _('North America')),
    ('SA', _('South America')),
    ('AN', _('Antarctica')),
)
