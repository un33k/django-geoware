from django.utils.translation import ugettext as _

from slugify import slugify

from .base import models


class Currency(models.Model):
    """
    Currency Model Class.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(
        _('Name'),
        max_length=254,
        null=True,
        blank=True,
    )

    slug = models.CharField(
        _('Slug'),
        max_length=254,
        null=True,
        blank=True,
    )

    code = models.CharField(
        _('Code'),
        db_index=True,
        max_length=40,
    )

    symbol = models.CharField(
        _('Symbol'),
        max_length=40,
        null=True,
        blank=True,
    )

    fractional_unit = models.CharField(
        _('Fractional Unit'),
        max_length=40,
        null=True,
        blank=True,
    )

    fractional_ratio = models.PositiveIntegerField(
        _('Fractional Ration'),
        default=0,
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
        db_table = '{app}-{type}'.format(app=app_label, type='currency')
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')
        unique_together = (('name', 'code'), )

    def save(self, *args, **kwargs):
        self.slug = slugify('{name}-{code}'.format(name=self.name, code=self.code))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
