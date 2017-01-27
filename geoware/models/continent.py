from django.utils.translation import ugettext as _

from .base import models
from .base import AbstractLocation


class Continent(AbstractLocation):
    """
    Continent Model Class.
    """
    code = models.CharField(
        _("Code"),
        db_index=True,
        max_length=2,
    )

    iso_n = models.CharField(
        'M49',
        db_index=True,
        max_length=3,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='continent')
        verbose_name = _('Continent')
        verbose_name_plural = _('Continents')
        unique_together = [('name', 'code')]

    @property
    def parent(self):
        return None
