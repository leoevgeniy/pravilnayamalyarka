from django.shortcuts import render
from .models import Category, SubCategory
from crm.forms import OrderForm

# Create your views here.

def index(request):
    catalog = {}
    categories = Category.objects.all()
    form = OrderForm
    for category in categories:
        subCategory = SubCategory.objects.filter(category=category)
        subcat = []
        for sub in subCategory:
            subcat.append(sub.name)
        catalog.update({category.name: subcat})
    dict = {
        'catalog': catalog,
        'form': form,
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
