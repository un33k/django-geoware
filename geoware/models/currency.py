from django.utils.translation import ugettext_lazy as _

from slugify import slugify

from .base import models


class Currency(models.Model):
    """
    Currency Model Class.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(
        _('LOCATION.CURRENCY.NAME'),
        max_length=254,
        null=True,
        blank=True,
    )

    slug = models.CharField(
        _('LOCATION.CURRENCY.SLUG'),
        max_length=254,
        null=True,
        blank=True,
    )

    code = models.CharField(
        _('LOCATION.CURRENCY.CODE'),
        db_index=True,
        max_length=40,
    )

    symbol = models.CharField(
        _('LOCATION.CURRENCY.SYMBOL'),
        max_length=40,
        null=True,
        blank=True,
    )

    fractional_unit = models.CharField(
        _('LOCATION.CURRENCY.FRACTIONAL_UNIT'),
        max_length=40,
        null=True,
        blank=True,
    )

    fractional_ratio = models.PositiveIntegerField(
        _('LOCATION.CURRENCY.FRACTIONAL_RATIO'),
        default=0,
    )

    url = models.URLField(
        _('LOCATION.CURRENCY.URL'),
        max_length=254,
        null=True,
        blank=True,
    )

    info = models.TextField(
        _('LOCATION.CURRENCY.INFO_DETAILS'),
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        _('LOCATION.CURRENCY.ACTIVE'),
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='currency')
        verbose_name = _('LOCATION.CURRENCY')
        verbose_name_plural = _('LOCATION.CURRENCY#plural')
        unique_together = (('name', 'code'), )

    def save(self, *args, **kwargs):
        self.slug = slugify('{name}-{code}'.format(name=self.name, code=self.code))
        super().save(*args, **kwargs)
