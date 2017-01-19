from django.contrib import admin

from ..models import Country
from ..forms import CountryForm


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    form = CountryForm
    list_per_page = 25
    list_display = (
        'name',
        'code',
        'continent',
        'capital',
        'currency',
        'iso_3',
        'iso_n',
        'fips',
        'jurisdiction',
        'idc',
        'tld',
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
        'iso_3',
        'iso_n',
        'fips',
        'currency__name',
        'capital__name',
        'continent__name',
        'tld',
        'idc',
    ]
    filter_horizontal = ('neighbors', 'languages',)
    readonly_fields = (
        'geoname_id',
        'altnames',
    )
    ordering=('name',)
