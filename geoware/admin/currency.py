from django.contrib import admin


class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'symbol',
        'fractional_unit',
        'fractional_ratio',
        'slug',
        'url',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'name',
        'code',
    ]
    list_per_page = 25
    ordering=('code',)
