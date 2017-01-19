from django.contrib import admin

from ..models import Timezone


@admin.register(Timezone)
class TimezoneAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = (
        'name_id',
        'country',
        'gmt_offset',
        'dst_offset',
        'raw_offset',
        'is_active',
        'slug',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'id',
        'name_id',
        'country__name'
    ]
    ordering=('raw_offset', 'name_id',)
