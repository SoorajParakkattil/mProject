from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
#from django.http import http404
from django.template import loader
from .models import Product

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'list/index.html', context)

def detail(request,product_id):
    product=get_object_or_404(Product,product_id=product_id)
    return render(request, 'list/detail.html', {'product':product})
