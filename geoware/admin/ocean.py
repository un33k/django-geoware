from django.contrib import admin

from ..models import Ocean
from ..forms import OceanForm


@admin.register(Ocean)
class OceanAdmin(admin.ModelAdmin):
    form = OceanForm
    list_per_page = 25
    list_display = (
        'name',
        'depth',
        'depth_name',
        'area',
        'is_active',
        'slug',
        'url',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'name',
    ]
    readonly_fields = ('altnames',)
    ordering=('name',)
