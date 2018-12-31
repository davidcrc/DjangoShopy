# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product
# Create your views here.


def hello_world(request):
    # return render(request, 'index.html')

    product = Product.objects.order_by('id')
    template = loader.get_template("index.html")
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))
    # Revisar como enviaba antes a un archivo index.html los datos desde aqui
