from django.contrib import admin

from ..models import City
from ..forms import CityForm

from .. import defaults as defs


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    form = CityForm
    list_per_page = 25
    list_display = (
        'geoname_id',
        'name',
        'slug',
        'division',
        'subdivision',
        'country',
        'population',
        'elevation',
        'area',
        'timezone',
        'district_of',
        'url',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'geoname_id',
        'name',
        'division__name',
        'subdivision__name',
        'country__name',
    ]
    filter_horizontal = ('altnames',)
    readonly_fields = (
        'altnames',
    )
    ordering = ('country', 'name',)
