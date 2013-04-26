from django.contrib import admin

class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
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
    list_per_page = 25
