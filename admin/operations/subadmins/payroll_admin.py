from django.contrib import admin
from django.http import HttpResponse
from operations.models import *
from authuser.models import *

# from operations.submodels.store_model import Stores


@admin.register(PayRoll)
class PayrollAdmin(admin.ModelAdmin):
    pass
    # list_display = ['name', 'email', 'phone','branch']

    def response_add(self, request, obj, post_url_continue) -> HttpResponse:
        if request.user.is_superuser:
            return True
        return False

