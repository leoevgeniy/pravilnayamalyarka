from django.contrib import admin

# Register your models here.
from crm.models import Order, StatusCrm, CommentCrm, OrderItems


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0
    fields = ('name', 'qty', 'price', 'cost',)
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'


class CommentsInline(admin.TabularInline):
    model = CommentCrm
    extra = 0
    fields = ('comment_text', 'comment_owner', 'comment_dt',)
    readonly_fields = ('comment_dt', 'comment_owner',)


@admin.register(Order)
class OrderAdm(admin.ModelAdmin):
    list_display = ('order_dt', 'order_name', 'order_phone', 'order_type', 'order_status', 'get_items',)
    list_display_links = ('order_dt', 'order_name', 'order_phone',)
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
        OrderItemsInline,
        CommentsInline,

    ]
    list_filter = ('order_status', )

    def get_items(self, obj):
        text = ""
        for i in obj.orderitems.all():
            text = text + '\n' + i.name + ' - ' + str(i.qty) + 'штук(и)'
        return text

    get_items.allow_tags = True
    get_items.short_description = 'Товары в заказе'

    def save_related(self, request, form, formsets, change):
        for formset in formsets:
            list_comment = formset.save(commit=False)
            for comment in list_comment:
                comment.comment_owner = request.user
        return super().save_related(request, form, formsets, change)



# admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(StatusCrm)


# @admin.register(CommentCrm)
# class CommentCRMAdmin(admin.ModelAdmin):
#     fields = ('comment_binding', 'comment_owner', 'comment_text', 'comment_dt',)
#     readonly_fields = ('comment_owner', 'comment_dt',)
#
#
#     def save_model(self, request, obj, form, change):
#         obj.comment_owner = request.user
#         obj.save()
