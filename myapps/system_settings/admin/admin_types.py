from django.contrib import admin

# Register your models here.

from system_settings.models.model_types import Types




@admin.register(Types)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name','type']