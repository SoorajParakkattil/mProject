from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view() , name='index'),
    url(r'^register/$', views.UserFormView.as_view() , name='register'),
     #product/product_id
       url(( r'^(?P<pk>[0-9]+)/$'), views.DetailView.as_view(), name='detail'),
      #Create the product
      url(r'^add/$', views.ProductCreate.as_view() , name='productadd'),

     url(r'^(?P<pk>[0-9]+)/update/$', views.ProductUpdate.as_view() , name='productup'),

      url(r'^(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view() , name='productdel'),
]
