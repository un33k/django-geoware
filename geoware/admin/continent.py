from django.contrib import admin

from ..models import Continent


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
        'iso_n',
        'population',
        'area',
        'is_active',
        'slug',
        'geoname_id',
        'url',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'geoname_id',
        'name',
        'code',
    ]
    list_per_page = 25
    readonly_fields = ('geoname_id', 'altnames', )
    ordering=('name', )
