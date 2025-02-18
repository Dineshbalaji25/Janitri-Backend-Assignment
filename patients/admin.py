from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Patient)
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'name','age')
        }),
    )