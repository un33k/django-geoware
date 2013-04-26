from django.db import models
from django.utils.translation import gettext as _
from django.utils.encoding import force_unicode

from .. import defaults

__all__ = ['Currency']

class Currency(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    name = models.CharField(_('Currency name'), max_length=254, blank=True, null=True)
    code = models.CharField(_('Currency code'), max_length=40, db_index=True)
    symbol = models.CharField(_('Currency Symbol'), max_length=40, blank=True, null=True)
    slug = models.CharField(_('Slug'), max_length=254, blank=True, null=True)
    fractional_unit = models.CharField(_('Fractional Unit'), max_length=40, blank=True, null=True)
    fractional_ratio = models.PositiveIntegerField(_('Fractional Ratio'), default=0)
    url = models.URLField(_("URL"), max_length=254, blank=True, null=True)
    is_active = models.BooleanField(_('Active'), default=True)

    def __unicode__(self):
        return force_unicode(self.name)
        
    class Meta:
        app_label = 'geoware'
        db_table = app_label + '-currency'
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')
        unique_together = (('name','code'), )

    def save(self, *args, **kwargs):
        s = self.name
        if self.code:
            s += '-' + self.code
        self.slug = defaults.slugify(self.name)
        super(Currency, self).save(*args, **kwargs)



