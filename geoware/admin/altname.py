from django.contrib import admin


class AltnameAdmin(admin.ModelAdmin):
    list_display = (
        'geoname_id',
        'ref_geoname_id',
        'name',
        'slug',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'geoname_id',
        'ref_geoname_id',
        'name',
        'language__name',
    ]
    list_per_page = 25
    ordering=('geoname_id', 'language__name', 'name',)
