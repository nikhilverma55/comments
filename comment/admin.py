from django.contrib import admin
from comment.models import (
    Product,
    Order,
    Comment
)


class ProductAdmin(admin.ModelAdmin):
    """
    Database represetation for Product schema
    """
    list_display = ['id']


class OrderAdmin(admin.ModelAdmin):
    """
    Database represetation for Order schema
    """
    list_display = ['id', 'amount', 'user']
    filter_horizontal = ['products']


class CommentAdmin(admin.ModelAdmin):
    """
    Database represetation for Order schema
    """
    list_display = ['id', 'active']
    search_field = ['comment_text']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
