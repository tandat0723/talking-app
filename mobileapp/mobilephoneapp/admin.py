from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, Category, Brand, Product, Banner, Storage, Ram, Color, Tag, ProductView, Comment, Like, Rate, \
    Delivery, Order, OrderDetail


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date']
    list_filter = ['name', 'created_date', 'updated_date']
    search_fields = ['name']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_date', 'updated_date']
    list_filter = ['name', 'category', 'created_date', 'updated_date']
    search_fields = ['name']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    readonly_fields = ['images']

    def images(self, img):
        if img:
            return mark_safe('<img src="/static/{url}" width="200px"/>'.format(url=img.image.name))


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'created_date', 'updated_date']
    list_filter = ['name', 'brand', 'created_date', 'updated_date']
    search_fields = ['name', 'brand']
    readonly_fields = ['images']

    def images(self, img):
        if img:
            return mark_safe('<img src="/static/{url}" width="200px"/>'.format(url=img.image.name))


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined']
    list_filter = ['date_joined']
    search_fields = ['date_joined']
    readonly_fields = ['avatars']

    def avatars(self, img):
        if img:
            return mark_safe('<img src="/static/{url}" width="200" />'.format(url=img.avatar.name))


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date']
    list_filter = ['name']
    search_fields = ['name']


class StorageAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date']
    list_filter = ['name']
    search_fields = ['name']


class RamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date']
    list_filter = ['name']
    search_fields = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date']
    list_filter = ['name']
    search_fields = ['name']


class ProductViewAdmin(admin.ModelAdmin):
    list_display = ['user', 'updated_date', 'views', 'product']
    list_filter = ['user', 'views', 'updated_date', 'product']
    search_fields = ['user', 'product']


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'created_date', 'updated_date']
    list_filter = ['name', 'updated_date']
    search_fields = ['name', 'phone']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'total', 'count']
    list_filter = ['product', 'count']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order', 'quantity', 'total', 'created_date', 'updated_date']
    list_filter = ['order', 'total', 'created_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'product', 'created_date', 'updated_date']
    list_filter = ['user', 'product', 'created_date', 'updated_date']
    search_fields = ['user', 'product']


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_date', 'updated_date', 'active']
    list_filter = ['user', 'product']
    search_fields = ['user', 'product']


class RateAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_date', 'updated_date', 'rate']
    list_filter = ['user', 'product']
    search_fields = ['user', 'product']


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ProductView, ProductViewAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Rate, RateAdmin)
