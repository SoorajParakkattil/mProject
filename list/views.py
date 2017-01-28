from django.views import generic
from .models import Product

class IndexView(generic.ListView):
    template_name='list/index.html'
    context_object_name='all_products'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):

    model=Product
    template_name='list/detail.html'
