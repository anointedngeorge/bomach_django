from django.contrib import admin

# Register your models here.

from settings.submodels.model_types import Types




@admin.register(Types)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name','type']