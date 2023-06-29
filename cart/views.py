from django.shortcuts import render
import json
# Create your views here.
# from networkx.generators.tests.test_small import null

from cart.forms import OrderConfirmForm
from cms.models import Product
from crm.models import Order, OrderItems, StatusCrm
from telebot.sendmessage import send_telegram


def cart(request):
    try:
        data = json.loads(request.COOKIES.get('cart'))
    except:
        data = []
    ids = []
    for cart_item in data:
        # print(cart_item)
        try:
            product = Product.objects.get(vendor_code=cart_item['id'])
            ids.append({'product': product, 'qty': cart_item['qty']})
        except:
            pass
    form = OrderConfirmForm
    return render(request, 'main/cart.html', {'products': ids, 'form': form})


def orderCreate(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        if request.COOKIES.get('cart') and len(request.COOKIES.get('cart')) > 0:
            cart = json.loads(request.COOKIES.get('cart'))
            status = StatusCrm.objects.get(status_name__exact='Новая')
            order = Order.objects.create(
                order_name=name,
                order_phone=phone,
                order_type='Заказ товара',
                order_status=status,

            )
            for item in cart:
                product = Product.objects.get(vendor_code=item['id'])

                orderItem = OrderItems.objects.create(
                    product=product,
                    order=order,
                    name=product.name,
                    qty=item['qty'],
                    price=product.price,
                    image=product.photo,
                    vendor_code=item['id'],
                    cost=item['qty']*product.price,

                )
        send_telegram(name, phone)
    response = render(request, 'main/thanks_page.html')
    response.delete_cookie('cart')

    return response


def orderView(request, pk):
    pass
