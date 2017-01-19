from django.contrib import admin

from ..models import Division
from ..forms import DivisionForm


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    form = DivisionForm
    list_per_page = 25
    list_display = (
        'name',
        'code',
        'country',
        'capital',
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
        'country__name',
        'capital__name',
    ]
    readonly_fields = (
        'geoname_id',
        'altnames',
    )
    ordering=('country', 'code',)
