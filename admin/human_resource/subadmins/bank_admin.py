from django.contrib import admin
from human_resource.models import *
import uuid


@admin.register(DrawingBank)
class DrawingBankAdmin(admin.ModelAdmin):
    list_display = ['title', 'code', 'action']
    exclude = ['code']

    def response_add(self, request, obj, post_url_continue=None):
        c =  uuid.uuid4().hex
        obj.code =  f"{c}"
        obj.save()
        return super().response_add(request, obj, post_url_continue)