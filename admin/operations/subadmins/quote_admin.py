from django.contrib import admin
from operations.models import *


@admin.register(QuotesModel)
class NameAdmin(admin.ModelAdmin):
    # list_display = ('',)
    pass

    # class Media:
    #     js = ('/admin/static/custom/custom.js/',)
        