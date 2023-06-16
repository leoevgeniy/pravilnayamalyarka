from django.contrib import admin

# Register your models here.
from crm.models import Order, StatusCrm, CommentCrm

admin.site.register(Order)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
