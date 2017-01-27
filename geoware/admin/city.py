from django.contrib import admin

from ..models import City
from ..forms import CityForm

from .. import defaults as defs


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    form = CityForm
    list_per_page = 25
    list_display = (
        'name',
        'country',
        'division',
        'subdivision',
        'population',
        'elevation',
        'area',
        'timezone',
        'district_of',
        'geoname_id',
        'slug',
        'url',
        'is_active',
        'updated_at',
        'created_at',
    ) + defs.GEOWARE_COORDINATES_FORMAT

    search_fields = [
        'geoname_id',
        'name',
        'division__name',
        'subdivision__name',
        'country__name',
    ]
    readonly_fields = (
        'geoname_id',
        'altnames',
    )
    ordering = ('country', 'name',)
