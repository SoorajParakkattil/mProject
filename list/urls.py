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
      url(r'loginpage',views.login , name='login'),
      #signup processing
      url(r'signup',views.signupprocess , name='signupprocess'),
      #Signup page
      url(r'signuppage',views.signup , name='signup'),
      #logout page
      url(r'logout' , views.logout , name='logout'),
      #processing login
      url(r'login',views.loginprocess , name = 'loginprocess'),

     #cart

     url(r'cart' , views.cart , name='cart'),
]
