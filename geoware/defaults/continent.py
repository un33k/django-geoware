from django.utils.translation import ugettext as _

GEOWARE_GEONAME_CONTINENT_DATA = [
    {
        'code': 'AF',
        'name': 'Africa',
        'geoname_id': '6255146'
    },
    {
        'code': 'AS',
        'name': 'Asia',
        'geoname_id': '6255147'
    },
    {
        'code': 'EU',
        'name': 'Europe',
        'geoname_id': '6255148'
    },
    {
        'code': 'NA',
        'name': 'North America',
        'geoname_id': '6255149'
    },
    {
        'code': 'OC',
        'name': 'Oceania',
        'geoname_id': '6255151'
    },
    {
        'code': 'SA',
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
