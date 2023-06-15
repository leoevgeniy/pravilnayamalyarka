from django.shortcuts import render
from .models import Category, SubCategory


# Create your views here.

def index(request):
    catalog = {}
    categories = Category.objects.all()
    for category in categories:
        subCategory = SubCategory.objects.filter(category=category)
        subcat=[]
        for sub in subCategory:
            subcat.append(sub.name)
        catalog.update({category.name: subcat})
    dict = {
        'catalog': catalog
    }
    for cat in catalog:
        for subcat in catalog[cat]:
            print(subcat)
    return render(request, 'index.html', dict)


def category(request, category):
    category = Category.objects.get(name=category)
    subCategory = SubCategory.objects.filter(category=category)
    dict = {
        'category': category,
        'subcategory': subCategory
    }
    return render(request, 'category.html', dict)
