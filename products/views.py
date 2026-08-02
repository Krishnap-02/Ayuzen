from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def home(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={
        'products':products,
        'category':categories
    }
    return render(request,'home.html',context)


def product_detail(request,id):
    product=Product.objects.get(id=id)
    context={
        'product':product
    }

    return render(request,'product_detail.html',context)


def category_products(request,id):
    category=Category.objects.all()
    products=Product.objects.filter(category_id=id)
    context={
            'products':products,
            'category':category
        }
    return render(request,'home.html',context)