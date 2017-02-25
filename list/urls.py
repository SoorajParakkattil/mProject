from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView, name='index'),

     #product/product_id
       url(( r'^(?P<pk>[0-9]+)/$'), views.DetailView.as_view(), name='detail'),
      #Create the product
      url(r'^add/$', views.ProductCreate.as_view() , name='productadd'),

     url(r'^(?P<pk>[0-9]+)/update/$', views.ProductUpdate.as_view() , name='productup'),

      url(r'^(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view() , name='productdel'),
      #login page redirectin
      url(r'^loginpage',views.login , name='login'),
      #signup processing
      url(r'^signup',views.signupprocess , name='signupprocess'),
      #Signup page
      url(r'^signuppage',views.signup , name='signup'),
      #logout page
      url(r'^logout' , views.logout , name='logout'),
      #processing login
      url(r'^login',views.loginprocess , name = 'loginprocess'),
      #orders
      url(r'^orders$',views.order , name = 'order'),
      url(r'^orders_new$',views.order_new , name = 'order_new'),

      url(r'^bill$',views.bill , name = 'bill'),

     #cart

     url(r'^cart' , views.cart , name='cart'),

     #add to cart
     url(( r'^addcart/(?P<pk>[0-9]+)/$'), views.addcart, name='addcart'),
     url(( r'^purchase/(?P<pk>[0-9]+)/$'), views.purchase_confirm, name='purchase'),
     url(( r'^response/(?P<pk>[0-9]+)/$'), views.order_confirm, name='response'),
     url(( r'^response_change/(?P<pk>[0-9]+)/$'), views.response_change, name='response_change'),
]
