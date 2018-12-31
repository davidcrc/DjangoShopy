# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Product
# Register your models here.


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    # Otra forma de retornar para que aparexca en el titulo
    list_display = ('name', 'description', 'category', 'price')

    list_filter = ('category', )
