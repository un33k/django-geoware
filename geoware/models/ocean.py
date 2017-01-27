from django.utils.translation import ugettext as _

from .base import models
from .base import AbstractLocation


class Ocean(AbstractLocation):
    """
    Ocean Model Class.
    """
    depth = models.PositiveIntegerField(
        _("Depth"),
        null=True,
        blank=True,
    )

    depth_name = models.CharField(
        _("Depth Name"),
        max_length=254,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='ocean')
        verbose_name = _('Ocean')
        verbose_name_plural = _('Oceans')
        unique_together = (('name'), )

    @property
    def parent(self):
        return None
