from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Customer, Product, Category, Order
# Register your models here.

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields =   {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class Productdmin(admin.ModelAdmin):
    list_display	=	['title','price','product_pic']

class CustomerAdmin(admin.ModelAdmin):
	list_display	=	['business_name','date_created','profile_pic',]

class OrderAdmin(admin.ModelAdmin):
    list_display    =   ['name_of_customer', 'product','ordered_on', 'Updated_at']

			
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, Productdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
	