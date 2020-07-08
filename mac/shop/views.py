from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def index(request):
    productlist = Product.objects.all()
    n = len(productlist)
    nslides = n // 4 + 1 if n % 4 != 0 else n // 4
    print(nslides, range(1, nslides))
    params = {'product': productlist, 'no_of_slides': nslides, 'range': range(nslides)}
    return render(request, 'shop/index.html', params)
    # return render(request, 'shop/base.html')
    # return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("CONTACT US")


def search(request):
    return HttpResponse("search US")


def productView(request):
    productlist = Product.objects.all()
    n = len(productlist)
    nslides = n // 4 + 1 if n % 4 != 0 else n // 4
    print(nslides)
    print(nslides, range(1, nslides))
    params = {'product': productlist, 'no_of_slides': nslides, 'range': range(nslides)}
    return render(request, 'shop/prodcutview.html', params)


def Allproduct(request, id):
    # productlist = Product.objects.all()
    # n = len(productlist)
    # nslides = n // 4 + 1 if n % 4 != 0 else n // 4
    # print(nslides)
    # print(nslides, range(1, nslides))
    # params = {'product': productlist, 'no_of_slides': nslides, 'range': range(nslides)}
    prod = Product.objects.filter(id=id)
    print(prod)
    return render(request, 'shop/product.html',{'prod':prod[0]})


def categorywiseproductView(request):
    # products = Product.objects.all()
    #

    #
    allprods = []
    catProd = Product.objects.values('category','id')
    cats = {item['category'] for item in catProd}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + 1 if n % 4 != 0 else n // 4
        allprods.append([prod, range(1, nslides), nslides])
    params = {'allprods': allprods}
    return render(request, 'shop/categoryWiseProduct.html', params)


def tracker(request):
    return HttpResponse("tracker")


def checkout(request):
    return HttpResponse("checkout")

# def readData(request):
#
#     params = ['name':Product.product_name,'price':Product.price,'description':Product.description]
#     return render(request,'view.html',params)
