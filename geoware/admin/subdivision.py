from django.contrib import admin

from ..models import Subdivision
from ..forms import SubdivisionForm


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    form = SubdivisionForm
    list_per_page = 25
    list_display = (
        'name',
        'division',
        'capital',
        'code',
        'fips',
        'population',
        'area',
        'is_active',
        'geoname_id',
        'slug',
        'url',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'name',
        'division__name',
        'division__country__name'
    ]
    readonly_fields = (
        'geoname_id',
        'altnames',
    )
    ordering=('division__country__name', 'division__name', 'name')
