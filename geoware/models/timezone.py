from django.utils.translation import ugettext as _

from slugify import slugify

from .base import models


class Timezone(models.Model):
    """
    Timezone Model Class.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    country = models.ForeignKey(
        "Country",
        verbose_name=_("LOCATION.TIMEZONE.COUNTRY"),
        related_name='%(app_label)s_%(class)s_country',
        null=True,
        blank=True,
    )

    name_id = models.CharField(
        _("LOCATION.TIMEZONE.ID"),
        db_index=True,
        max_length=254,
    )

    slug = models.CharField(
        _('LOCATION.TIMEZONE.SLUG'),
        max_length=254,
        null=True,
        blank=True,
    )

    gmt_offset = models.FloatField(
        _("LOCATION.TIMEZONE.OFFSET_GMT_JAN_1"),
        default=0.0,
    )

    dst_offset = models.FloatField(
        _("LOCATION.TIMEZONE.OFFSET_DST_JUL_1"),
        default=0.0,
    )

    raw_offset = models.FloatField(
        _("LOCATION.TIMEZONE.OFFSET_RAW"),
        default=0.0,
    )

    url = models.URLField(
        _('LOCATION.TIMEZONE.URL'),
        max_length=254,
        null=True,
        blank=True,
    )

    info = models.TextField(
        _('LOCATION.TIMEZONE.INFO_DETAILS'),
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        _('LOCATION.TIMEZONE.ACTIVE'),
        default=True,
    )

    def __str__(self):
        return self.name_id

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='timezone')
        verbose_name = _('LOCATION.TIMEZONE')
        verbose_name_plural = _('LOCATION.TIMEZONE#plural')

    def get_absolute_url(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify('{name}'.format(name=self.name))
        super().save(*args, **kwargs)
