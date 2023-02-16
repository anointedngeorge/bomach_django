from django.contrib import admin

# Register your models here.

from settings.submodels.model_gallery import *
from settings.submodels.model_service import *



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    pass