from django.contrib import admin


class ContinentAdmin(admin.ModelAdmin):
    filter_horizontal = ('altnames',)
    list_display = (
        'id',
        'geoname_id',
        'name',
        'slug',
        'code',
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
        'code',
    ]
    list_per_page = 25
