from django.contrib import admin


class SubdivisionAdmin(admin.ModelAdmin):
    filter_horizontal = ('altnames',)
    list_display = (
        'geoname_id',
        'name',
        'slug',
        'division',
        'population',
        'area',
        'url',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'name',
        'division__name',
        'division__country__name'
    ]
    readonly_fields = (
        'capital',
        'division',
        'altnames',
    )
    list_per_page = 25
    ordering=('division__country__name','division__name','name')
