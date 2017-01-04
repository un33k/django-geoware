from django.contrib import admin

class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
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
        'id',
        'name',
        'code',
    ]
    list_per_page = 25
