from django.contrib import admin
from .. import defaults

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    list_display = (
        'id',
        'geoname_id',
        'name', 
        'slug',
        'region',
        'subregion',
        'country',
        'population',
        'elevation',
        'area', 
        'timezone', 
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
        'region__name',
        'subregion__name',
        'country__name',
    ]
    list_per_page = 25