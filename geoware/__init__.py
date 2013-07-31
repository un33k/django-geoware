
__version__ = '0.0.6'

import defaults

if defaults.GEOWARE_INCLUDE_TEMPLATE_TAGS:
    from django import template
    application_tags = [
        'geoware.templatetags.geoip',
    ]
    for t in application_tags: template.add_to_builtins(t)



