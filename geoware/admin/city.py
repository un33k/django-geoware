from django.contrib import admin
from .. import defaults as defs


class CityAdmin(admin.ModelAdmin):
    filter_horizontal = ('altnames',)
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
    readonly_fields = (
        'district_of',
        'division',
        'subdivision',
        'altnames',
    )
    list_per_page = 25
    ordering = ('country', 'name',)
