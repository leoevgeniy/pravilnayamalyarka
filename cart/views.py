from django.shortcuts import render
import json
# Create your views here.


from cms.models import Product


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
    return render(request, 'main/cart.html', {'products': ids})
