from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    '''Display fields in the admin panel'''
    list_display = (
        'name',
        'category',
        'market_price',
        'rating',
        'image'
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    '''Display fields in the admin panel'''
    list_display = (
        'friendly_name',
        'name',
    )


# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
