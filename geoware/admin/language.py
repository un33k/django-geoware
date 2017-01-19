from django.contrib import admin

from ..models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = (
        'code',
        'name',
        'slug',
        'percent',
        'dialect',
        'is_active',
        'url',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'name',
        'code',
    ]
    ordering=('code',)
