from django.shortcuts import render

from cms.forms import UploadFileForm
from cms.models import Product, Service, PromoSlider
from crm.models import Order, StatusCrm
from .models import Category, SubCategory, ServiceCategory
from crm.forms import OrderForm
from telebot.sendmessage import send_telegram


# Create your views here.

def index(request):
    promos = PromoSlider.objects.all()
    services_category = ServiceCategory.objects.all()
    disc = {
        'promoslider': promos,
        'services_category': services_category,
    }
    return render(request, 'main/index.html', disc)


def goods(request):
    catalog = {}
    categories = Category.objects.all()
    form = OrderForm
    up = UploadFileForm
    for category in categories:
        subCategory = SubCategory.objects.filter(category=category)
        subcat = []
        for sub in subCategory:
            subcat.append(sub.name)
        catalog.update({category.name: subcat})
    dict = {
        'catalog': catalog,
        'form': form,
        'up': up,
    }

    return render(request, 'main/goods.html', dict)


def services(request):
    catalog = {}
    categories = ServiceCategory.objects.all()
    # form = OrderForm
    # up = UploadFileForm
    for category in categories:
        services = Service.objects.filter(service_category=category)
        currentservices = []
        for ser in services:
            currentservices.append(ser)
        catalog.update({category.name: currentservices})
    dict = {
        'catalog': catalog,
    }

    return render(request, 'main/services.html', dict)


def category(request, category):
    category = Category.objects.get(name=category)
    subCategory = SubCategory.objects.filter(category=category)
    dict = {
        'category': category,
        'subcategory': subCategory
    }
    return render(request, 'main/category.html', dict)


def subcategory(request, category, subcategory):
    category = Category.objects.get(name=category)
    subCategory = SubCategory.objects.get(name=subcategory)
    products = Product.objects.filter(subcategory=subCategory)
    dict = {
        'category': category,
        'subcategory': subCategory,
        'products': products,
    }
    return render(request, 'main/subcategory.html', dict)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    status = StatusCrm.objects.get(status_name__exact='Новая')
    element = Order(order_name=name, order_phone=phone, order_type='Заказ обратного звонка', order_status=status)
    element.save()
    send_telegram(name, phone)
    return render(request, 'main/thanks_page.html', {'name': name})
