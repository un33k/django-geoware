from django.utils.translation import ugettext_lazy as _

from slugify import slugify

from .base import models


class Language(models.Model):
    """
    Language Model Class.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(
        _("LOCATION.LANGUAGE.NAME"),
        max_length=254,
        null=True,
        blank=True,
    )

    slug = models.CharField(
        _('LOCATION.LANGUAGE.SLUG'),
        max_length=254,
        null=True,
        blank=True,
    )

    code = models.CharField(
        _("LOCATION.LANGUAGE.CODE"),
        db_index=True,
        max_length=40,
    )

    percent = models.FloatField(
        _("LOCATION.LANGUAGE.WORLDWIDE_PERCENTAGE"),
        null=True,
        blank=True,
    )

    dialect = models.CharField(
        _("LOCATION.LANGUAGE.DIALECT"),
        max_length=254,
        null=True,
        blank=True,
    )

    url = models.URLField(
        _('LOCATION.LANGUAGE.URL'),
        max_length=254,
        null=True,
        blank=True,
    )

    info = models.TextField(
        _('LOCATION.LANGUAGE.INFO_DETAILS'),
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        _('LOCATION.LANGUAGE.ACTIVE'),
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'geoware'
        db_table = '{app}-{type}'.format(app=app_label, type='language')
        verbose_name = _('LOCATION.LANGUAGE')
        verbose_name_plural = _('LOCATION.LANGUAGE#plural')
        unique_together = (('name', 'code'), )

    def save(self, *args, **kwargs):
        self.slug = slugify('{name}-{code}'.format(name=self.name, code=self.code))
        super().save(*args, **kwargs)
