from django.contrib import admin

from .models import Admin

def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)

make_published.short_description = 'Mark as published'

class AdminAdmin(admin.ModelAdmin):
    fields = ['name', 'photo', 'is_published']
    list_display = ['id', 'name', 'is_published']
    ordering = ['-id']
    list_filter = ['created_at', 'name']
    actions = [make_published]
    # exclude = ..
admin.site.register(Admin, AdminAdmin)