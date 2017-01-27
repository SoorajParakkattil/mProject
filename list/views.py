from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    all_products=Product.objects.all()
    html=''
    for product in all_products:
        url=''+str(product.product_id)+'/'
        html+='<a href="'+ url +'">'+ product.pname +'</a><br>'
    return HttpResponse(html)
def detail(request,product_id):
    return HttpResponse("<h1>hello"+str(product_id) +"</ h1>")
