from django.contrib import admin

from ..models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = (
        'code',
        'name',
        'symbol',
        'fractional_unit',
        'fractional_ratio',
        'is_active',
        'slug',
        'url',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'name',
        'code',
    ]
    ordering=('code',)
