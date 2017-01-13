from django.apps import apps
from django.apps import AppConfig as DjangoAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(DjangoAppConfig):
    """
    Configuration entry point for the geoware app.
    """
    label = name = 'geoware'
    verbose_name = _("GEOWARE.APPLICATION")
