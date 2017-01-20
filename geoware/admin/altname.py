from django.contrib import admin

from ..models import Altname
from ..forms import AltnameForm


@admin.register(Altname)
class AltnameAdmin(admin.ModelAdmin):
    form = AltnameForm
    list_per_page = 25
    list_display = (
        'ref_geoname_id',
        'name',
        'language',
        'geoname_id',
        'is_active',
        'slug',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'geoname_id',
        'ref_geoname_id',
        'name',
        'language__name',
    ]
    ordering=('ref_geoname_id', 'language__name', 'name',)
