
from django.utils.encoding import force_unicode
from django.db import models
from django.utils.translation import gettext as _

from .. import defaults

__all__ = [ 'Altname']

class Altname(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    language = models.ForeignKey('Language', related_name='%(app_label)s_%(class)s_language', null=True, blank=True)
    name = models.CharField(_('Alternative Name'), max_length=254, db_index=True)
    is_preferred = models.BooleanField(_('Is Preferred Name'), default=True)
    is_short = models.BooleanField(_('Is Short Name'), default=True)
    geoname_id = models.CharField(max_length=50, db_index=True, null=True, blank=True)
    ref_geoname_id = models.CharField(max_length=50, db_index=True, null=True, blank=True)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        app_label = 'geoware'
        db_table = app_label + '-altname'

    def __unicode__(self):
        return force_unicode(self.name)

    def get_absolute_url(self):
        return defaults.slugify(self.name)


