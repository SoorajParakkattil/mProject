from django.views import generic
from .models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name='list/index.html'
    context_object_name='all_products'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):

    model=Product
    template_name='list/detail.html'
class ProductCreate (CreateView):
    model=Product
    fields=['pname','product_id','price','quantity','product_type','brand_name','mrp','expiry','vat','effective_price']
