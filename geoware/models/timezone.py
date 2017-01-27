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
        verbose_name=_("Country"),
        related_name='%(app_label)s_%(class)s_country',
        null=True,
        blank=True,
    )

    name_id = models.CharField(
        _("Name"),
        db_index=True,
        max_length=254,
    )

    slug = models.CharField(
        _('Slug'),
        max_length=254,
        null=True,
        blank=True,
    )

    gmt_offset = models.FloatField(
        _("GMT Offset (Jan 1)"),
        default=0.0,
    )

    dst_offset = models.FloatField(
        _("DST Offset (Jul 1)"),
        default=0.0,
    )

    raw_offset = models.FloatField(
        _("Raw Offset"),
        default=0.0,
    )

    url = models.URLField(
        _('URL'),
        max_length=254,
        null=True,
        blank=True,
    )

    info = models.TextField(
        _('Details'),
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='timezone')
        verbose_name = _('Timezone')
        verbose_name_plural = _('Timezones')
        unique_together = [('name_id',)]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_id
