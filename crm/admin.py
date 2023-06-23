from django.contrib import admin

# Register your models here.
from crm.models import Order, StatusCrm, CommentCrm, OrderItems
class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0
    fields = ('name', 'qty', 'price', 'cost', )
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'


class CommentsInline(admin.TabularInline):
    model = CommentCrm
    extra = 0
    fields = ('comment_text', 'comment_dt', )
    readonly_fields = ('comment_dt', )

@admin.register(Order)
class OrderAdm(admin.ModelAdmin):
    list_display = ('order_name', 'order_phone', 'order_type', 'order_status', 'get_items', )
    fields = (
            'order_name',
            'order_phone',
            'order_type',
            'order_status',
        )
    #     'Товары', {
    #     'get_items_arr',
    # }

    inlines = [
        CommentsInline,
        OrderItemsInline,
    ]

    def get_items(self, obj):
        text = ""
        for i in obj.orderitems.all():
            text = text + '\n' + i.name + ' - ' + str(i.qty) + 'штук(и)'
        return text

    get_items.allow_tags = True


# admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
