
from django.contrib import admin
from django.http import HttpResponse
from operations.models import *
# from operations.submodels.store_model import Stores


@admin.register(Stores)
class StoreAdmin(admin.ModelAdmin):
    pass
    # list_display = ['name', 'email', 'phone','branch']


@admin.register(StoreExpenditure)
class StoreExpenditureAdmin(admin.ModelAdmin):
    

    def response_add(self, request, obj, post_url_continue=None) -> HttpResponse:
        store =  obj.store.unit_price.amount
        qty =  obj.store.qty
        amt =  obj.store.amount.amount
        # print(store)
        # print(qty)
        # print(amt)
        return super().response_add(request, obj, post_url_continue)
