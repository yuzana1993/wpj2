from django.contrib import admin
from .models import Sellrecord


class SellrecordAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_phone','price','showroom','paid','date']
    list_filter = ['customer_name','customer_phone','price','showroom','paid','date']
    search_fields =['customer_name','customer_phone','price','showroom','paid','date']

admin.site.register(Sellrecord, SellrecordAdmin)    