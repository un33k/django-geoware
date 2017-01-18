Django Geoware
====================

**A Django application for handling GIS related data**

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]

Overview
====================

**Enables** Django-powered site to handle GIS related data while keeping it **DRY**.


How to install
====================

    1. easy_install django-geoware
    2. pip install django-geoware
    3. git clone http://github.com/un33k/django-geoware
        a. cd django-geoware
        b. run python setup.py
    4. wget https://github.com/un33k/django-geoware/zipball/master
        a. unzip the downloaded file
        b. cd into django-geoware-* directory
        c. run python setup.py


How to use
====================

   ```python
    # Add `geoware` to your INSTALLED_APPS in the settings file.
    # Run python manage.py migrate

    # `manage.py` without any arguments will show geoware's of available commands.
    #[geoware]
    #   country     # down/loads all countries
    #   timezone    # down/loads all timezones
    #   division    # down/loads all available divisions (admin level 1)
    #   subdivision # down/loads all available subdivisions (admin level 2)
    #   city        # down/loads all cities with population greater 1000
    #   hierarchy   # down/loads hierarchies - cities & districts
    #   altname     # down/loads names in alternative languages for locations
    #   geo         # down/loads all of the above commands in proper order

    # Note: all currencies, languages, continents & oceans are automatically loaded
    # when executing any of the above commands

    # Note 2: all locations will have a 'lat', 'lng' fields. If you are using GIS.
    # Please refer to the `advanced users` sections for info on how to enable GIS.
   ```

Advanced users:
====================
   ```python
    # If you are using GeoDjango with a gis enabled database, then
    # put the following in your configuration to enable GIS in geoware.
    GEOWARE_USING_GIS = True
    MIGRATION_MODULES = {'geoware': 'geoware.migrations_gis'}

    # Add `geoware` to your INSTALLED_APPS in the settings file.
    # Run python manage.py migrate

    # Note 1: all the commands in the `How to use` sections can be used to load and
    # update your data from geoname's website.

    # Note 2: all locations will have a 'point' fields when gis is enabled.
    # All downloaded files are cached in user's home directory under  `.geoware`.
    # You can overwrite the cache directory by setting `GEOWARE_DATA_DIR` in your
    # settings.py
   ```

Running the tests
====================

To run the tests against the current environment:

    python manage.py test


License
====================

Released under a ([MIT](LICENSE)) license.


Version
====================
X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.

[status-image]: https://secure.travis-ci.org/un33k/django-geoware.png?branch=master
[status-link]: http://travis-ci.org/un33k/django-geoware?branch=master

[version-image]: https://img.shields.io/pypi/v/django-geoware.svg
[version-link]: https://pypi.python.org/pypi/django-geoware

[coverage-image]: https://coveralls.io/repos/un33k/django-geoware/badge.svg
[coverage-link]: https://coveralls.io/r/un33k/django-geoware

[download-image]: https://img.shields.io/pypi/dm/django-geoware.svg
[download-link]: https://pypi.python.org/pypi/django-geoware
