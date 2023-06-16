import os


import xlrd
from django.http import HttpResponse
from django.shortcuts import render
import openpyxl
from openpyxl_image_loader import SheetImageLoader

# Create your views here.
from cms.forms import UploadFileForm
from cms.models import WorkPhoto, Product
from main.models import SubCategory, Category
from pravilnayamalyarka.settings import BASE_DIR, MEDIA_ROOT


def photomigrations(request):
    col_dir = BASE_DIR + '/materials/photo/'
    col = os.listdir(col_dir)
    for img in col:
        work = WorkPhoto.objects.create(
            name='',
            photo='images/donework/' + img,
        )

    return render(request, 'thanks_page.html')


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
            image=''
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

                        image = image_loader.get('C'+str(row+1))
                    except:
                        pass
                    line[worksheet.cell(row, 0).value] = params
                    rows.append(line)
                    # print(worksheet.cell(row, 0).value, line.keys())
                    if Product.objects.filter(vendor_code=str(params[0])).exists():
                        product = Product.objects.get(vendor_code=str(params[0]))
                        image.save(MEDIA_ROOT+'/images/'+str(params[0]) + '.png', format='png')
                    else:
                        image.save(MEDIA_ROOT+'/images/'+str(params[0]) + '.png', format='png')
                        if SubCategory.objects.filter(name=cat).exists:
                            subcategory = SubCategory.objects.get(name=cat)
                            category = Category.objects.get(name=subcategory.category)
                            product = Product.objects.create(
                                category=category,
                                subcategory=subcategory,
                                photo='images/'+ str(params[0]) + '.png',
                                name=str(params[1]),
                                description=str(params[3]),
                                vendor='ROLLINGDOG',
                                vendor_code=str(params[0]),
                                price=int(params[4]),
                                rrc=int(params[5]),
                                availability=str(params[6]),
                                pack=str(params[7])

                            )
                # if Product.objects.get(vendor_code=)

        return HttpResponse('готово')
