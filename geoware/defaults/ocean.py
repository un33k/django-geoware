from django.utils.translation import ugettext as _

GEOWARE_GEONAME_OCEAN_DATA = [
    {
        'name_std': 'Arctic',
        'name': 'Arctic',
    },
    {
        'name_std': 'Atlantic',
        'name': 'Atlantic',
    },
    {
        'name_std': 'Indian',
        'name': 'Indian',
    },
    {
        'name_std': 'Pacific',
        'name': 'Pacific',
    },
    {
        'name_std': 'Southern',
        'name': 'Southern',
    },
]

GEOWARE_OCEAN_CHOICES = (
    ('Arctic', _('Arctic')),
    ('Atlantic', _('Atlantic')),
    ('Indian', _('Indian')),
    ('Pacific', _('Pacific')),
    ('Southern', _('Southern')),
)
