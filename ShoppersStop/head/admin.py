from django.contrib import admin
from .models import *

class ImageTublerinline(admin.TabularInline):
    model = Images


class TagTublerinline(admin.TabularInline):
    model = Tag


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageTublerinline,TagTublerinline]

class OrderItemTubleinline(admin.TabularInline):
    model = OrderItem   

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTubleinline]

# Register your models here.
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)