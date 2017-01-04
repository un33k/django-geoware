from django.utils.translation import ugettext as _

from .base import models
from .base import AbstractLocation


class Ocean(AbstractLocation):
    """
    Ocean Model Class.
    """
    depth = models.PositiveIntegerField(
        _("LOCATION.OCEAN.DEPTH_MAX"),
        null=True,
        blank=True,
    )

    depth_name = models.CharField(
        _("LOCATION.OCEAN.DEPTH_MAX_NAME"),
        max_length=254,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='ocean')
        verbose_name = _('LOCATION.OCEAN')
        verbose_name_plural = _('LOCATION.OCEAN#plural')

    @property
    def parent(self):
        return None
