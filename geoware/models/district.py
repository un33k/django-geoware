from django.utils.translation import ugettext_lazy as _

from .base import models
from .base import AbstractCity


class District(AbstractCity):
    """
    Continent Model Class.
    """
    city = models.ForeignKey(
        'City',
        verbose_name=_("LOCATION.DISTRICT"),
        related_name='%(app_label)s_%(class)s_city',
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='district')
        verbose_name = _('LOCATION.DISTRICT')
        verbose_name_plural = _('LOCATION.DISTRICT#plural')
        unique_together = [('name', 'city')]

    @property
    def parent(self):
        if self.city:
            return self.city
        return None
