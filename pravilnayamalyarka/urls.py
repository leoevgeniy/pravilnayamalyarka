"""
URL configuration for pravilnayamalyarka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import cart.views
import cms.views as cmsviews
import main.views as views
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('category/<str:category>', views.category, name='category'),
    path('category/<str:category>/<str:subcategory>', views.subcategory, name='subcategory'),
    path('product/<str:pk>', cmsviews.product_view, name='product_view'),
    path('chaining/', include('smart_selects.urls')),
    path('thanks', views.thanks_page, name='thanks'),
    path('migratephoto/', cmsviews.photomigrations, name='photomigrations'),
    path('migratexlsx/', cmsviews.productsimport, name='migratexlsx'),
    path('cart/', cart.views.cart, name='cart'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
    # path(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root': os.path.join(SITE_ROOT, 'static')})
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
