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
    # Read docs and populate your database with the provided utility commands
   ```


Advanced users:
====================


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
