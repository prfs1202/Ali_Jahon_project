from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from apps.models import Category, Product, ProductImage, User, SiteSettings, Order, CanceledOrder, NewOrder

admin.site.site_header = "Alijahon Admin"
admin.site.index_title = "Welcome to Alijahon Portal"
admin.site.register(User)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = 'slug',


class ProductImageInline(StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    exclude = 'slug',
    inlines = ProductImageInline,
    list_display = 'name', 'is_exists'
    search_fields = 'name', 'price',
    ordering = '-created_at',
    list_filter = 'quantity',

    fieldsets = (
        ("Page 1",
         {"fields":
              ("description",
               "price",
               "payment",
               "quantity",
               )
          }),
        ("Page 2",
         {"fields": (
             'for_stream_price',
             'tg_id',
             'category')}
         ),
    )

    @admin.display(empty_value="?")
    def is_exists(self, obj):
        icon_url = 'https://img.icons8.com/?size=100&id=9fp9k4lPT8us&format=png&color=000000'
        if not obj.quantity:
            icon_url = 'https://img.icons8.com/?size=100&id=63688&format=png&color=000000'
        return format_html("<img src='{}' style='width: 30px' />", icon_url)


@admin.register(SiteSettings)
class SiteSettingsModelAdmin(ModelAdmin):
    pass


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    pass


@admin.register(CanceledOrder)
class DeliveredOrderAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status=Order.StatusType.DELIVERED)


@admin.register(NewOrder)
class NewOrderAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status=Order.StatusType.NEW)
