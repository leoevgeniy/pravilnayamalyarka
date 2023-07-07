from django.shortcuts import render
import json
# Create your views here.
# from networkx.generators.tests.test_small import null

from cart.forms import OrderConfirmForm
from cms.forms import SearchForm
from cms.models import Product, Logo, Packprice, Contacts, Socials
from crm.models import Order, OrderItems, StatusCrm
from telebot.sendmessage import send_telegram


def cart(request):
    try:
        logo = Logo.objects.get(inuse=True)
    except:
        logo = ''
    searchform = SearchForm
    try:
        data = json.loads(request.COOKIES.get('cart'))
    except:
        data = []
    ids = []
    try:
        contacts = Contacts.objects.all()
    except:
        contacts = ''
    for cart_item in data:
        try:
            product = Product.objects.get(vendor_code=cart_item['id'])
            weight = Packprice.objects.get(id=cart_item['weight'])
            cost = weight.price * cart_item['qty']
            ids.append({'product': product, 'qty': cart_item['qty'], 'weight': weight, 'cost': cost})
        except:
            pass
    form = OrderConfirmForm
    socials = Socials.objects.all()

    content = {
        'socials': socials,
        'products': ids,
        'form': form,
        'searchform': searchform,
        'logo': logo,
        'contacts': contacts[0],
    }

    return render(request, 'main/cart.html', content)


def orderCreate(request):
    try:
        logo = Logo.objects.get(inuse=True)
    except:
        logo = ''
    searchform = SearchForm

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
                weight = int(item['weight'])
                weightObject = Packprice.objects.get(id=weight)
                orderItem = OrderItems.objects.create(
                    product=product,
                    order=order,
                    name=product.name,
                    qty=item['qty'],
                    weight=weightObject,
                    price=weightObject.price,
                    image=product.photo,
                    vendor_code=item['id'],
                    cost=item['qty']*weightObject.price,

                )
        send_telegram(name, phone)
    socials = Socials.objects.all()
    try:
        contacts = Contacts.objects.all()
    except:
        contacts = ''

    content = {
        'socials': socials,
        'searchform': searchform,
        'logo': logo,
        'contacts': contacts[0],
    }

    response = render(request, 'main/thanks_page.html', content)
    response.delete_cookie('cart')

    return response


def orderView(request, pk):
    pass
