from django.contrib import admin

from .models import *
admin.site.site_header = "keep your dick up"
admin.site.site_title = "keep your dick up"
admin.site.index_title = "keep your dick up"



admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
