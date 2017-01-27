from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
     #product/product_id
       url(( r'^(?P<product_id>[0-9]+)/$'), views.detail, name='detail'),
]
