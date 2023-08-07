from django.contrib import admin

from apps.product.models import *


class ProductImageAdmin(admin.StackedInline):
    model = ProductImages


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_published')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageAdmin]

    class Meta:
        model = Products


admin.site.register(ProductCategory)
