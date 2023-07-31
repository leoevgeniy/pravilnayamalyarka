from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
# Register your models here.
from cms.models import Product, Packprice
from crm.models import Order, StatusCrm, CommentCrm, OrderItems


# class OutfitForm(forms.ModelForm):
#     products = forms.ModelMultipleChoiceField(
#         required=False,
#         queryset=Product.objects.all(),
#         widget=FilteredSelectMultiple("Товары", is_stacked=False),
#         label='')


class OrderItemsInline(admin.StackedInline):
    model = OrderItems
    # raw_id_fields = ('order',)
    extra = 0
    fields = ('name', 'product', )
    show_change_link = ('product', )
    readonly_fields = ('name', )
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'



class CommentsInline(admin.TabularInline):
    model = CommentCrm
    extra = 0
    show_change_link = ('comment_text', )
    fields = ('comment_text', 'comment_owner', 'comment_dt',)
    readonly_fields = ('comment_dt', 'comment_owner',)


@admin.register(Order)
class OrderAdm(admin.ModelAdmin):
    # form = OutfitForm
    list_display = ('order_dt', 'order_name', 'order_phone', 'order_type', 'order_status', 'get_items',)
    list_display_links = ('order_dt', 'order_name', 'order_phone',)
    fields = (
        'order_name',
        'order_phone',
        'order_type',
        'order_status',
        # 'products',
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

            text = text + '\n' + i.product.name + ' - ' + str(i.qty) + 'штук(и)'
        return text

    get_items.allow_tags = True
    get_items.short_description = 'Товары в заказе'

    def save_related(self, request, form, formsets, change):
        for formset in formsets:
            list_comment = formset.save(commit=False)
            for comment in list_comment:
                comment.comment_owner = request.user
        return super().save_related(request, form, formsets, change)

@admin.register(OrderItems)
class OrderItemsAdm(admin.ModelAdmin):
    list_display = ('product', 'order')
    list_filter = ('order', )
    exclude = ('image', 'vendor_code', )

    def render_change_form(self, request, context, *args, **kwargs):
        try:
            print(context['object_id'])
            orderitem = OrderItems.objects.get(id=int(context['object_id']))
            context['adminform'].form.fields['weight'].queryset = Packprice.objects.filter(
                product__name__icontains=orderitem.product.name
            )
        except:
            pass
        return super(OrderItemsAdm, self).render_change_form(request, context, *args, **kwargs)


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
