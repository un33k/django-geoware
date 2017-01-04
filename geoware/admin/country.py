from django.contrib import admin

class CountryAdmin(admin.ModelAdmin):
    filter_horizontal = ('altnames', 'neighbors', 'languages',)
    list_display = (
        'id',
        'geoname_id',
        'name',
        'slug',
        'code',
        'iso_3',
        'iso_n',
        'fips',
        'capital',
        'currency',
        'continent',
        'jurisdiction',
        'idc',
        'tld',
        'population',
        'area',
        'url',
        'absolute_url',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'id',
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
    readonly_fields = ('altnames', 'languages',)
    list_per_page = 25
