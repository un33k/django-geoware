from django.contrib import admin
from .. import defaults as defs


class DistrictAdmin(admin.ModelAdmin):
    filter_horizontal = ('altnames',)
    list_display = (
        'id',
        'geoname_id',
        'name',
        'slug',
        'city',
        'population',
        'area',
        'url',
        'absolute_url',
        'is_active',
        'updated_at',
        'created_at',
    )
    if defs.GEOWARE_USING_GIS:
        list_display += ('point',)
    else:
        list_display += ('lng', 'lng',)

    search_fields = [
        'id',
        'name',
        'city__name',
        'city__country__name',
    ]
    readonly_fields = ('altnames',)
    list_per_page = 25
