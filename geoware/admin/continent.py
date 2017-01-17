from django.contrib import admin


class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        'geoname_id',
        'name',
        'slug',
        'code',
        'iso_n',
        'population',
        'area',
        'url',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'geoname_id',
        'name',
        'code',
    ]
    list_per_page = 25
    readonly_fields = ('altnames',)
    ordering=('name',)
