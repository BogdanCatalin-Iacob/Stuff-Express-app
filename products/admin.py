from django.contrib import admin
from .models import Product, Category, Review


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


class ReviewAdmin(admin.ModelAdmin):
    '''
    Display review fields in admin panel
    '''
    list_display = (
        'user',
        'product',
        'date',
        'review_text',
        'star_rating',
    )


# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
