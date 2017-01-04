from django.contrib import admin


class SubregionAdmin(admin.ModelAdmin):
    filter_horizontal = ('altnames',)
    list_display = (
        'id',
        'geoname_id',
        'name',
        'slug',
        'region',
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
        'region__name',
        'region__country__name'
    ]
    readonly_fields = ('altnames',)
    list_per_page = 25
