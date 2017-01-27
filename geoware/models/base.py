
from django.utils.translation import ugettext as _

from slugify import slugify

from .. import defaults as defs

if defs.GEOWARE_USING_GIS:
    from django.contrib.gis.db import models
    from django.contrib.gis.geos import Point
else:
    from django.db import models


class AbstractBaseLocation(models.Model):
    """
    Base Abstract Model for all location types.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(
        _('Name'),
        db_index=True,
        max_length=254,
    )

    slug = models.CharField(
        _('Slug'),
        max_length=254,
        blank=True,
        null=True
    )

    name_std = models.CharField(
        _('Standard Name'),
        max_length=254,
        blank=True,
        null=True,
    )

    area = models.PositiveIntegerField(
        _('Area (Square KM)'),
        default=0,
    )

    population = models.PositiveIntegerField(
        _('Population'),
        default=0
    )

    elevation = models.IntegerField(
        _('Elevation'),
        default=0,
    )

    geoname_id = models.CharField(
        db_index=True,
        unique=True,
        max_length=50,
        null=True,
        blank=True,
    )

    altnames = models.ManyToManyField(
        'Altname',
        verbose_name=_('Altname'),
        related_name='%(app_label)s_%(class)s_altnames',
        blank=True,
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
        abstract = True

    @property
    def hierarchy(self):
        tree = self.parent.hierarchy if self.parent else []
        tree.append(self)
        return tree

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        hierarchy = '-'.join(reversed([hi.name for hi in self.hierarchy]))
        self.slug = slugify(hierarchy)
        super().save(*args, **kwargs)


if defs.GEOWARE_USING_GIS:
    class AbstractLocation(AbstractBaseLocation):
        objects = models.GeoManager()

        class Meta:
            abstract = True
else:
    class AbstractLocation(AbstractBaseLocation):
        objects = models.Manager()

        class Meta:
            abstract = True


class AbstractBaseCity(AbstractLocation):
    """
    Base Abstract for all cities.
    """
    bbw = models.FloatField(
        _("Bounding Box West"),
        default=0.0,
    )

    bbn = models.FloatField(
        _("Bounding Box North"),
        default=0.0,
    )

    bbe = models.FloatField(
        _("Bounding Box East"),
        default=0.0,
    )

    bbs = models.FloatField(
        _("Bounding Box South"),
        default=0.0,
    )

    class Meta:
        abstract = True


if defs.GEOWARE_USING_GIS:
    class AbstractCity(AbstractBaseCity):
        point = models.PointField(
            _('Point'),
            default='POINT(0.0 0.0)',
        )

        class Meta:
            abstract = True
else:
    class AbstractCity(AbstractBaseCity):
        lat = models.FloatField(
            _('Latitude'),
            default=0.0,
        )

        lng = models.FloatField(
            _('Longitude'),
            default=0.0,
        )

        class Meta:
            abstract = True
