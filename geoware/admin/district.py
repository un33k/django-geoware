from django.contrib import admin
from .. import defaults

class DistrictAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
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
    if defaults.GEOWARE_USING_GEO_DJANGO:
        list_display += ('point',) 
    else:
        list_display += ('lng', 'lng',) 

    search_fields = [
        'id',
        'name',
        'city__name',
        'city__country__name',
    ]
    list_per_page = 25
