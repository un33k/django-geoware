
from django.utils.encoding import force_unicode
from django.db import models
from django.utils.translation import gettext as _

from .. import defaults as defs


class Timezone(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    name_id = models.CharField(_('Timezone ID'), max_length=254, db_index=True)
    gmt_offset = models.FloatField(_('GMT offset 1. Janu'), default=0.0)
    dst_offset = models.FloatField(_('DST offset 1. Jul'), default=0.0)
    raw_offset = models.FloatField(_('RAW offset'), default=0.0)

    country = models.ForeignKey('Country', related_name='%(app_label)s_%(class)s_country', null=True, blank=True)
    slug = models.CharField(_('Slug'), max_length=254, blank=True, null=True)
    url = models.URLField(_("URL"), max_length=254, blank=True, null=True)
    info = models.TextField(_('Information Details'), blank=True)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        app_label = 'geoware'
        db_table = app_label + '-timezone'

    def __unicode__(self):
        return force_unicode(self.name_id)

    def get_absolute_url(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = defs.slugify(self.name_id)
        super(Timezone, self).save(*args, **kwargs)




