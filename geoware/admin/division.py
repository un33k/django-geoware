from django.contrib import admin


class DivisionAdmin(admin.ModelAdmin):
    filter_horizontal = ('altnames',)
    list_display = (
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
        'name',
        'country__name',
        'capital__name',
    ]
    readonly_fields = (
        'capital',
        'altnames',
    )
    list_per_page = 25
    ordering=('country','code',)
