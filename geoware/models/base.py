
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
        _('FIELDS.NAME'),
        db_index=True,
        max_length=254,
    )

    slug = models.CharField(
        _('LOCATION.SLUG'),
        max_length=254,
        blank=True,
        null=True
    )

    name_std = models.CharField(
        _('LOCATION.NAME_STD.FIELD'),
        max_length=254,
        blank=True,
        null=True,
    )

    area = models.PositiveIntegerField(
        _('LOCATION.AREA_SQUARE_KM'),
        default=0,
    )

    population = models.PositiveIntegerField(
        _('LOCATION.POPULATION'),
        default=0
    )

    elevation = models.IntegerField(
        _('LOCATION.ELEVATION_METERS'),
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
        verbose_name=_('LOCATION.ALTNAME'),
        related_name='%(app_label)s_%(class)s_altnames',
        blank=True,
    )

    url = models.URLField(
        _('LOCATION.URL'),
        max_length=254,
        null=True,
        blank=True,
    )

    info = models.TextField(
        _('LOCATION.INFO_DETAILS'),
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        _('LOCATION.ACTIVE'),
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
        hierarchy = '-'.join(self.hierarchy.reverse())
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
        _("LOCATION.CITY.BOUNDING.BOX.WEST"),
        default=0.0,
    )

    bbn = models.FloatField(
        _("LOCATION.CITY.BOUNDING.BOX.NORTH"),
        default=0.0,
    )

    bbe = models.FloatField(
        _("LOCATION.CITY.BOUNDING.BOX.EAST"),
        default=0.0,
    )

    bbs = models.FloatField(
        _("LOCATION.CITY.BOUNDING.BOX.SOUTH"),
        default=0.0,
    )

    class Meta:
        abstract = True


if defs.GEOWARE_USING_GIS:
    class AbstractCity(AbstractBaseCity):
        point = models.PointField(
            _('LOCATION.CITY.POINT'),
            default='POINT(0.0 0.0)',
        )

        class Meta:
            abstract = True
else:
    class AbstractCity(AbstractBaseCity):
        lat = models.FloatField(
            _('LOCATION.CITY.LATITUDE'),
            default=0.0,
        )

        lng = models.FloatField(
            _('LOCATION.CITY.LONGITUDE'),
            default=0.0,
        )

        class Meta:
            abstract = True
