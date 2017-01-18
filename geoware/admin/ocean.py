from django.contrib import admin


class OceanAdmin(admin.ModelAdmin):
    filter_horizontal = ('altnames',)
    list_display = (
        'name',
        'slug',
        'population',
        'area',
        'url',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'name',
    ]
    readonly_fields = ('altnames',)
    list_per_page = 25
    ordering=('name',)
