from django.utils.translation import ugettext_lazy as _

from .base import models
from .base import AbstractLocation


class Continent(AbstractLocation):
    """
    Continent Model Class.
    """
    code = models.CharField(
        _("LOCATION.CONTINENT.CODE"),
        db_index=True,
        max_length=2,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='continent')
        verbose_name = _('LOCATION.CONTINENT')
        verbose_name_plural = _('LOCATION.CONTINENT#plural')
        unique_together = [('name', 'code')]

    @property
    def parent(self):
        return None
