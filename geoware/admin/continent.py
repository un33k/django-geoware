from django.contrib import admin

from ..models import Continent


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = (
        'name',
        'code',
        'iso_n',
        'population',
        'area',
        'is_active',
        'geoname_id',
        'slug',
        'url',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'geoname_id',
        'name',
        'code',
    ]
    readonly_fields = ('geoname_id', 'altnames', )
    ordering=('name', )
