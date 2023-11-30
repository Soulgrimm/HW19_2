from django.shortcuts import render

from catalog.models import Product


def index(request):
    products_list = Product.objects.all()
    content = {
        'object_list': products_list
    }
    return render(request, 'main/index.html', content)


def contacts(request):
    return render(request, 'main/contacts.html')
