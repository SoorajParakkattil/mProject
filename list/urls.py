from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view() , name='index'),
     #product/product_id
       url(( r'^(?P<pk>[0-9]+)/$'), views.DetailView.as_view(), name='detail'),
      #Create the product
      url(r'add/$', views.ProductCreate.as_view() , name='productadd'),
]
