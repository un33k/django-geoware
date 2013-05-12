from django.db import models
from django.utils.translation import gettext as _
from django.utils.encoding import force_unicode

from .. import defaults

__all__ = ['Language']

class Language(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    name = models.CharField(_('Language name'), max_length=254, blank=True, null=True)
    code = models.CharField(_("Language code"), max_length=40, db_index=True)
    slug = models.CharField(_('Slug'), max_length=254, blank=True, null=True)
    percent = models.FloatField(_('Worldwide percentage'), blank=True, null=True)
    dialect = models.CharField(max_length=254, blank=True, null=True)
    url = models.URLField(_("URL"), max_length=254, blank=True, null=True)
    info = models.TextField(_('Information Details'), blank=True)
    is_active = models.BooleanField(_('Active'), default=True)

    def __unicode__(self):
        return force_unicode(self.name)
        
    class Meta:
        app_label = 'geoware'
        db_table = app_label + '-language'
        # ordering = ('name', 'dialect', 'slug', 'percent',)

    def save(self, *args, **kwargs):
        if self.name:
            s = self.name
            if self.dialect:
                s += '-' + self.dialect
            self.slug = defaults.slugify(self.name)
        super(Language, self).save(*args, **kwargs)



