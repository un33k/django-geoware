from django.utils.translation import ugettext as _

from slugify import slugify

from .base import models


class Altname(models.Model):
    """
    Currency Model Class.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    language = models.ForeignKey(
        'Language',
        verbose_name=_('LOCATION.ALTNAME.LAGUAGUE'),
        related_name='%(app_label)s_%(class)s_language',
        null=True,
        blank=True,
    )

    name = models.CharField(
        _('LOCATION.ALTNAME.NAME'),
        db_index=True,
        max_length=254,
    )

    slug = models.CharField(
        _('LOCATION.ALTNAME.SLUG'),
        max_length=254,
        blank=True,
        null=True
    )

    geoname_id = models.CharField(
        db_index=True,
        unique=True,
        max_length=50,
        null=True,
        blank=True,
    )

    ref_geoname_id = models.CharField(
        db_index=True,
        max_length=50,
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        _('LOCATION.ALTNAME.ACTIVE'),
        default=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='altname')
        verbose_name = _('LOCATION.ALTNAME')
        verbose_name_plural = _('LOCATION.ALTNAME#plural')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
