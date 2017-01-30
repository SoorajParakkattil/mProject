from django.views import generic
from .models import Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from .forms import UserForms
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import views

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

class ProductUpdate (UpdateView):
    model=Product
    fields=['pname','product_id','price','quantity','product_type','brand_name','mrp','expiry','vat','effective_price']

class ProductDelete (DeleteView):
    model=Product
    success_url=reverse_lazy('index')

class UserFormView(views):
    form_class=UserForms
    template_name='list/registratin_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})



    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)

            if user is not None :
                if user.is_active():
                    login(request,user)
                    return redirect('index')
        return render(request,self.template_name,{'form':form})
