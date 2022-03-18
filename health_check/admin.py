from django.contrib import admin

# Register your models here.
from health_check.models import Application, Status


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'name_tag', 'ativo']


@admin.register(Status)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['application', 'code']

