"""
This is the module that handles admin side of the checkout app.
"""
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Allows the adding and editing of inline items from inside the order model.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Defines the order model in the admin.
    """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'order_total', 'grand_total',)

    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number',
              'country', 'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
