from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from upload.models import Product
admin.site.register(Product)
