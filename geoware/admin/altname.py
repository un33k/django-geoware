from django.contrib import admin

class AltnameAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'geoname_id',
        'name',
        'is_preferred', 
        'is_short',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'id',
        'geoname_id',
        'name',
        'language__name',
    ]
    list_per_page = 25


