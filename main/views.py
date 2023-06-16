from django.shortcuts import render

from cms.forms import UploadFileForm
from crm.models import Order
from .models import Category, SubCategory
from crm.forms import OrderForm
from telebot.sendmessage import send_telegram
# Create your views here.

def index(request):
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
    return render(request, 'index.html', dict)


def category(request, category):
    category = Category.objects.get(name=category)
    subCategory = SubCategory.objects.filter(category=category)
    dict = {
        'category': category,
        'subcategory': subCategory
    }
    return render(request, 'category.html', dict)


def subcategory(request, category, subcategory):
    category = Category.objects.get(name=category)
    subCategory = SubCategory.objects.get(name=subcategory)
    dict = {
        'category': category,
        'subcategory': subCategory
    }
    return render(request, 'subcategory.html', dict)

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    send_telegram(name, phone)
    return render(request, 'thanks_page.html', {'name': name})
