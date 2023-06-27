import os

import xlrd
from django.http import HttpResponseRedirect
from django.shortcuts import render
import openpyxl
from openpyxl_image_loader import SheetImageLoader

# Create your views here.
from cms.forms import UploadFileForm
from cms.models import WorkPhoto, Product, Service, Vendor
from main.models import SubCategory, Category, ServiceCategory
from pravilnayamalyarka.settings import BASE_DIR, MEDIA_ROOT


def product_view(request, pk):
    product = Product.objects.get(vendor_code=pk)
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"] = 123
        request.session.cycle_key()
    context = {
        "product": product
    }
    return render(request, 'main/product_details.html', context)


def photomigrations(request):
    col_dir = BASE_DIR + '/materials/photo/'
    col = os.listdir(col_dir)
    for img in col:
        work = WorkPhoto.objects.create(
            name='',
            photo='images/donework/' + img,
        )

    return render(request, 'main/thanks_page.html')


def productsimport(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            filehandle = request.FILES.get('file', False)

            pxl_doc = openpyxl.load_workbook(filehandle.temporary_file_path())
            sheet = pxl_doc['Прайс']
            workbook = xlrd.open_workbook(filehandle.temporary_file_path())
            worksheet = workbook.sheet_by_index(0)
            rows = []
            image_loader = SheetImageLoader(sheet)
            cat = ''
            image = ''
            for row in range(1, worksheet.nrows):
                line = {}
                if type(worksheet.cell(row, 0).value) == str and not worksheet.cell(row, 1).value:
                    cat = worksheet.cell(row, 0).value
                if type(worksheet.cell(row, 0).value) == float:
                    params = []
                    for column in range(worksheet.ncols):
                        params.append(worksheet.cell(row, column).value)
                    params.append(cat)
                    try:

                        image = image_loader.get('C' + str(row + 1))
                    except:
                        pass
                    line[worksheet.cell(row, 0).value] = params
                    rows.append(line)
                    # print(worksheet.cell(row, 0).value, line.keys())
                    if Product.objects.filter(vendor_code=params[0]).exists():
                        product = Product.objects.get(vendor_code=str(params[0]))
                        image.save(MEDIA_ROOT + '/images/' + str(params[0]) + '.png', format='png')
                    else:
                        image.save(MEDIA_ROOT + '/images/' + str(params[0]) + '.png', format='png')
                        if SubCategory.objects.filter(name=cat).exists:
                            subcategory = SubCategory.objects.get(name=cat)
                            category = Category.objects.get(name=subcategory.category)
                            try:
                                vendor = Vendor.objects.get(name='ROLLINGDOG')
                            except:
                                vendor = Vendor.objects.create(name='ROLLINGDOG')
                            product = Product.objects.create(
                                category=category,
                                subcategory=subcategory,
                                photo='images/' + str(params[0]) + '.png',
                                name=str(params[1]),
                                description=str(params[3]),
                                vendor=vendor,
                                vendor_code=int(params[0]),
                                price=int(params[4]),
                                rrc=int(params[5]),
                                availability=str(params[6]),
                                pack=str(params[7])

                            )
                # if Product.objects.get(vendor_code=)

        return HttpResponseRedirect('/admin/')


def services_import(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            filehandle = request.FILES.get('file', False)

            pxl_doc = openpyxl.load_workbook(filehandle.temporary_file_path())
            sheet = pxl_doc['Лист1']
            workbook = xlrd.open_workbook(filehandle.temporary_file_path())
            worksheet = workbook.sheet_by_index(0)
            rows = []
            cat = ''
            for row in range(1, worksheet.nrows):
                line = {}
                if type(worksheet.cell(row, 2).value) == str and not worksheet.cell(row, 1).value:
                    cat = worksheet.cell(row, 2).value

                if type(worksheet.cell(row, 1).value) == float:
                    params = []
                    for column in range(worksheet.ncols):
                        if column > 0:
                            params.append(worksheet.cell(row, column).value)
                    params.append(cat)
                    line[worksheet.cell(row, 1).value] = params
                    rows.append(line)
                    # print(worksheet.cell(row, 0).value, line.keys())
                    if Service.objects.filter(service_code=str(params[0])).exists():
                        service = Service.objects.get(service_code=str(params[0]))
                    else:
                        if ServiceCategory.objects.filter(name=cat).exists:
                            category = ServiceCategory.objects.get(name=cat)
                            service = Service.objects.create(
                                name=params[1],
                                service_pc=params[2],
                                service_price=params[5],
                                service_code=params[0],
                                service_category=category

                            )
                # if Product.objects.get(vendor_code=)

        return HttpResponseRedirect('/admin/')
