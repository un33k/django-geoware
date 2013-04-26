from django.contrib import admin

class SubregionAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    list_display = (
        'id',
        'geoname_id',
        'name', 
        'slug',
        'region',
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
        'region__name',
        'region__country__name'
    ]
    list_per_page = 25
