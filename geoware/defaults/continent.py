from django.utils.translation import ugettext as _

GEOWARE_GEONAME_CONTINENT_DATA = [
    {
        'code': 'AF',
        'name': 'Africa',
        'geonameId': '6255146'
    },
    {
        'code': 'AS',
        'name': 'Asia',
        'geonameId': '6255147'
    },
    {
        'code': 'EU',
        'name': 'Europe',
        'geonameId': '6255148'
    },
    {
        'code': 'NA',
        'name': 'North America ',
        'geonameId': '6255149'
    },
    {
        'code': 'OC',
        'name': 'Oceania',
        'geonameId': '6255151'
    },
    {
        'code': 'SA',
        'name': 'South America ',
        'geonameId': '6255150'
    },
    {
        'code': 'AN',
        'name': 'Antarctica',
        'geonameId': '6255152'
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
