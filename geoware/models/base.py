
from django.utils.encoding import force_unicode
from django.utils.translation import gettext as _

from .. import defaults

if defaults.GEOWARE_USING_GEO_DJANGO:
    from django.contrib.gis.db import models
    from django.contrib.gis.geos import Point
else:
    from django.db import models

__all__ = [ 'LocationBase', 'CityBase']

class LocationBase(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    name = models.CharField(_('Name'), max_length=254, db_index=True)
    name_std = models.CharField(_('Standard name'), max_length=254, blank=True, null=True)
    slug = models.CharField(_('Slug'), max_length=254, blank=True, null=True)
    area = models.PositiveIntegerField(_('Area in square kilometers'), default=0)
    population = models.PositiveIntegerField(_('Population'), default=0)
    elevation = models.PositiveIntegerField(_('Elevation in meters'), default=0)
    url = models.URLField(_("URL"), max_length=254, blank=True, null=True)
    geoname_id = models.CharField(max_length=50, db_index=True, null=True, blank=True)
    altnames = models.ManyToManyField('Altname', related_name='%(app_label)s_%(class)s_altnames', blank=True, null=True)
    info = models.TextField(_('Information Details'), blank=True)
    absolute_url = models.CharField(max_length=254, null=True, blank=True)
    is_active = models.BooleanField(_('Active'), default=True)

    objects = models.GeoManager() if defaults.GEOWARE_USING_GEO_DJANGO else models.Manager()

    class Meta:
        abstract = True

    @property
    def hierarchy(self):
        tree = self.parent.hierarchy if self.parent else []
        tree.append(self)
        return tree

    def __unicode__(self):
        return force_unicode(self.name)

    def build_absolute_url(self, overwrite=False, commit=True):
        if not self.absolute_url or overwrite:
            self.absolute_url = "/".join([self.slug, self.parent.get_absolute_url()]) if self.parent else self.slug
            if commit:
                self.save()
        return self.absolute_url

    def get_absolute_url(self):
        if not self.absolute_url:
            self.build_absolute_url()
        return self.absolute_url

    def _long_slug(self, forward=True):
        url = self.get_absolute_url()
        tokens = url.split('/') if forward else reversed(url.split('/'))
        return "-".join(tokens)

    @property
    def long_slug(self):
        return self._long_slug()

    @property
    def long_slug_reversed(self):
        return self._long_slug(forward=False)

    def save(self, *args, **kwargs):
        self.slug = defaults.slugify(self.name)
        self.build_absolute_url(overwrite=False)
        super(LocationBase, self).save(*args, **kwargs)


class CityBase(LocationBase):

    # bounding box
    bbw = models.FloatField(_("Bounding Box West"), default=0.0)
    bbn = models.FloatField(_("Bounding Box North"), default=0.0)
    bbe = models.FloatField(_("Bounding Box East"), default=0.0)
    bbs = models.FloatField(_("Bounding Box South"), default=0.0)

    if defaults.GEOWARE_USING_GEO_DJANGO:
        point = models.PointField(_('Point'), default='POINT(0.0 0.0)')
    else:
        # lat/lng of location
        lat = models.FloatField(_('Latitude'), default=0.0)
        lng = models.FloatField(_('Longitude'), default=0.0)

    class Meta:
        abstract = True






