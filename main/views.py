from django.shortcuts import render
from datetime import date
from cms.forms import UploadFileForm, SearchForm
from cms.models import Product, Service, PromoSlider, WorkPhoto, Logo, Introduction, Socials
from crm.models import Order, StatusCrm
from .models import Category, SubCategory, ServiceCategory
from crm.forms import OrderForm
from telebot.sendmessage import send_telegram
from PIL import Image
from pravilnayamalyarka.settings import BASE_DIR
# Create your views here.

def index(request):
    today = date.today()
    promos = PromoSlider.objects.filter(start_date__lte=today).filter(expiration_date__gte=today)
    services_category = ServiceCategory.objects.all()
    work = WorkPhoto.objects.all()
    work_landscape = []
    work_portrate = []
    for w in work:
        with Image.open(BASE_DIR + w.photo_url) as img:
            width, height = img.size
            if width/height >= 1.77 and len(work_landscape) < 11:
                work_landscape.append(w)
            elif width/height < 1 and len(work_portrate) < 11:
                work_portrate.append(w)
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    form = OrderForm
    searchform = SearchForm
    socials = Socials.objects.all()
    try:
        logo = Logo.objects.get(inuse=True)
    except:
        logo = ''
    try:
        intro = Introduction.objects.get(inuse=True)
    except:
        intro = ''

    disc = {
        'socials': socials,
        'logo': logo,
        'intro': intro,
        'work_landscape': work_landscape,
        'work_portrate': work_portrate,
        'categories': categories,
        'subcategories': subcategories,
        'promoslider': promos,
        'services_category': services_category,
        'form': form,
        'searchform': searchform,
    }
    return render(request, 'main/index.html', disc)


def goods(request):
    catalog = {}
    categories = Category.objects.all()
    form = OrderForm
    up = UploadFileForm
    searchform = SearchForm
    for category in categories:
        subCategory = SubCategory.objects.filter(category=category)
        subcat = []
        for sub in subCategory:
            subcat.append(sub.name)
        catalog.update({category.name: subcat})
    try:
        logo = Logo.objects.get(inuse=True)
    except:
        logo = ''
    dict = {
        'logo': logo,
        'searchform': searchform,
        'catalog': catalog,
        'form': form,
        'up': up,
    }

    return render(request, 'main/goods.html', dict)


def services(request):
    catalog = {}
    categories = ServiceCategory.objects.all()
    searchform = SearchForm
    # form = OrderForm
    # up = UploadFileForm
    for category in categories:
        services = Service.objects.filter(service_category=category)
        currentservices = []
        for ser in services:
            currentservices.append(ser)
        catalog.update({category.name: currentservices})
    try:
        logo = Logo.objects.get(inuse=True)
    except:
        logo = ''
    dict = {
        'logo': logo,
        'searchform': searchform,
        'catalog': catalog,
    }

    return render(request, 'main/services.html', dict)


def category(request, category):
    category = Category.objects.get(name=category)
    subCategory = SubCategory.objects.filter(category=category)
    searchform = SearchForm
    allcategory = Category.objects.all()
    allsubcategory = SubCategory.objects.all()
    try:
        logo = Logo.objects.get(inuse=True)
    except:
        logo = ''

    dict = {
        'logo': logo,
        'allcategory': allcategory,
        'allsubcategory': allsubcategory,
        'searchform': searchform,
        'category': category,
        'subcategory': subCategory
    }
    return render(request, 'main/category.html', dict)


def subcategory(request, category, subcategory, *args):
    vendor = ''
    sortup = ''
    sortdown = ''
    if request.GET.get('vendor') is not None:
        vendor = (request.GET.get('vendor'))
    if request.GET.get('sortup') is not None:
        sortup = (request.GET.get('sortup'))
    if request.GET.get('sortdown') is not None:
        sortdown = (request.GET.get('sortdown'))

    allcategory = Category.objects.all()
    allsubcategory = SubCategory.objects.all()

    category = Category.objects.get(name=category)
    subCategory = SubCategory.objects.get(name=subcategory)
    searchform = SearchForm
    # if sortup:
    products = Product.objects.filter(subcategory=subCategory).filter(vendor__name__icontains=vendor)
    productsJS = list(Product.objects.filter(subcategory=subCategory).filter(vendor__name__icontains=vendor).values())
    # products['weight'] = []
    # else:
    #     products = Product.objects.filter(subcategory=subCategory).filter(vendor__name__icontains=vendor).order_by('-price')
    # for product in products:
        # print(product.packprice)
    allbrend = []
    for product in Product.objects.filter(subcategory=subCategory):
        if product.vendor not in allbrend:
            allbrend.append(product.vendor)
    # productsJSData = json.dumps({'productsJS': productsJS})
    try:
        logo = Logo.objects.get(inuse=True)
    except:
        logo = ''

    dict = {
        'logo': logo,
        'searchform': searchform,
        'sortup': sortup,
        'sortdown': sortdown,
        'vendor': vendor,
        'allbrend': allbrend,
        'category': category,
        'subcategory': subCategory,
        'products': products,
        # 'productsJS': productsJSData,
        'allcategory': allcategory,
        'allsubcategory': allsubcategory,
    }
    return render(request, 'main/subcategory.html', dict)


def thanks_page(request):
    searchform = SearchForm
    name = request.POST['name']
    phone = request.POST['phone']
    status = StatusCrm.objects.get(status_name__exact='Новая')
    element = Order(order_name=name, order_phone=phone, order_type='Заказ обратного звонка', order_status=status)
    element.save()
    send_telegram(name, phone)
    try:
        logo = Logo.objects.get(inuse=True)
    except:
        logo = ''
    return render(request, 'main/thanks_page.html', {'name': name, 'searchform': searchform, 'logo': logo,})
