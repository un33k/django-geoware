from django.contrib import admin

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
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
    list_per_page = 25
