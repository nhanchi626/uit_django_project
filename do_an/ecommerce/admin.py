from django.contrib import admin
from .models import Role, User, ProductCategory, Product, Order, OrderDetail
# Register your models here.


admin.site.register(Role)
admin.site.register(User)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)