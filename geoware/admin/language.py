from django.contrib import admin


class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'slug',
        'percent',
        'dialect',
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
