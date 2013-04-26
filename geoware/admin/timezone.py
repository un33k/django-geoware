from django.contrib import admin

class TimezoneAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name_id',) }
    list_display = (
        'id',
        'name_id',
        'country',
        'gmt_offset', 
        'dst_offset',
        'raw_offset',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'id',
        'name_id',
        'country__name'
    ]
    list_per_page = 25


