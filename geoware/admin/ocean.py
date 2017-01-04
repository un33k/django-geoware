from django.contrib import admin

class OceanAdmin(admin.ModelAdmin):
    filter_horizontal = ('altnames',)
    list_display = (
        'id',
        'name',
        'slug',
        'population',
        'area',
        'url',
        'absolute_url',
        'is_active',
        'updated_at',
        'created_at',
    )
    search_fields = [
        'id',
        'name',
    ]
    readonly_fields = ('altnames',)
    list_per_page = 25
