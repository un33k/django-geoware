from django.contrib import admin


class RegionAdmin(admin.ModelAdmin):
    filter_horizontal = ('altnames',)
    list_display = (
        'id',
        'geoname_id',
        'name',
        'slug',
        'code',
        'capital',
        'country',
        'population',
        'area',
        'url',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'id',
        'name',
        'country__name',
        'capital__name',
    ]
    readonly_fields = ('altnames',)
    list_per_page = 25
