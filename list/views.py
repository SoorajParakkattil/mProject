from django.views import generic
from .models import Product,User,Batch,Purchase,Plist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from .forms import UserForms
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone

"""from django.views.generic import views"""



'''def IndexView(request):
    try:
        id = request.session['logid']
    except Exception:
        return render(request,'list/login.html',{'loginmessage' : 'Please Login to Continue'  })
    proList=Product.objects.all()
    return render(request, 'list/index.html',{'proList': proList })'''
def IndexView(request):
    try:
        id = request.session['logid']
    except Exception:
        return render(request,'list/login.html',{'loginmessage' : 'Please Login to Continue'  })
    proList=Product.objects.all()
    usrs=User.objects.all().filter(adm_no=id)
    for u in usrs:
        a=0
    if(u.isadmin==64):
        return render(request, 'list/index_admin.html',{'proList': proList })
    return render(request, 'list/index.html',{'proList': proList })

def purchase_confirm(request,pk):
    id=request.session['logid']
    remarks = request.POST.get("remarks","")
    uAll=User.objects.all().filter(adm_no=id)
    for u in uAll:
        a=0
    p=Purchase.objects.all().filter(purch_id=pk)
    for pu in p:
        a=0
    pu.remarks=remarks
    pu.placed=1
    pu.save()
    return redirect('/products')

def response_change(request,pk):

    p=Purchase.objects.all().filter(purch_id=pk)
    for pu in p:
        a=0
    pu.responded=0
    pu.save()
    return redirect('/products/orders')

def order_confirm(request,pk):
    response = request.POST.get("response","")
    p=Purchase.objects.all().filter(purch_id=pk)
    for pu in p:
        a=0
    pu.response=response
    pu.responded=1
    pu.save()
    return redirect('/products/orders')


def addcart(request,pk):
    id=request.session['logid']
    uAll=User.objects.all().filter(adm_no=id)
    for u in uAll:
        a=0
    pre=Product.objects.all().filter(product_id=pk)
    for pr in pre:
        a=0
    p=Purchase.objects.all()
    j=a
    pu=Purchase()
    for pu in p:
        if(pu.adm_no==u and pu.responded==0):
            a=1

    if(pu.responded!=0):
        a=0
    j=pu.total+pr.price
    if(a==0):
        pu=Purchase(adm_no=u,purchase_date=timezone.now(),total=pr.price,remarks='',response='',responded=0)

    j=0

    pu.save()
    pl=Plist(purch_id=pu,product_id=pr,price=pr.price,quantity=1)
    pl.save()
    pl=Plist.objects.all().filter(purch_id=pu.purch_id)
    for pls in pl:
        j=j+pls.price
    pu.total=j
    pu.save()

    return redirect('/products')


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

def login(request):
    return render(request, 'list/cart.html')

def logout(request):
    auth_logout(request)
    return redirect('/products/')

def order(request):
    p=Purchase.objects.all().filter(placed=1)
    l=Plist.objects.all()
    u=User.objects.all()
    product=Product.objects.all()
    return render(request, 'list/orders.html',{'u': u , 'p': p , 'l' : l, 'product' : product })

def order_new(request):
    p=Purchase.objects.all().filter(placed=1)
    l=Plist.objects.all()
    u=User.objects.all()
    product=Product.objects.all()
    return render(request, 'list/order_all.html',{'u': u , 'p': p , 'l' : l, 'product' : product })


def bill(request):
    id=request.session['logid']
    product=Product.objects.all()

    return render(request, 'list/bill.html',{'product' : product })

def cart(request):
    id=request.session['logid']
    p=Purchase.objects.all().filter(adm_no=id)
    product=Product.objects.all()
    i=Purchase()
    for i in p:
        a=0
    pl=Plist.objects.all().filter(purch_id=i.purch_id)

    return render(request, 'list/cart.html',{'k': i , 'pl' : pl, 'product' : product })

'''class Signup (CreateView):
    model=User
    fields=['name','adm_no','phone_no','password','cbid']'''
def signup(request):
	return render(request, 'list/signup.html' )

'''def logout(request):
    request.session['logid'] = ''
    request.session['vericode'] = ''
    return HttpResponseRedirect('/app')'''

def loginprocess(request):
	adm_no =  request.POST.get("username","")
	password = request.POST.get("password","")
	if(len(adm_no) == 0 and len(password) == 0):
		return render(request,'list/login.html',{'loginmessage' : ''  })
	user_data = User.objects.all().filter(adm_no = adm_no)
	got = True
	for e in user_data:
		got = False
	if(got):
		return render(request,'list/login.html',{'loginmessage' : 'Email id Does Not Exist Please Signup '})

	for e in user_data:
		if(e.password != password):
			return render(request,'list/login.html',{'loginmessage' : 'Password/Emailid entered is wrong please Try again' })
	'''if(_ver == 0):
		return render(request,'verified.html', {'id' : _id} )'''
	request.session['logid'] = adm_no
	return HttpResponseRedirect('/products')

def signupprocess(request):
    password = request.POST.get('password','')
    name = request.POST.get('name','')
    phone = request.POST.get('phonenumber','')
    cbid = request.POST.get('cbid','')
    '''vericode = '000000'
    verified = '0'	'''
    adm_no = request.POST.get('email','')
    val=1
    batch = Batch.objects.all()
    for i in batch:
        if(i.cbid == cbid): val=0;break
    dict = {'name' : name , 'batch': batch , 'phonenumber' : cbid,'cbid' : phone,'adm_no' : adm_no, 'message' : 'Error'}
    if(password == '' or  password.__len__() >= 100 or password.__len__() <= 7):
        dict['signupmessage'] = "Enter a valid password ** It should contain more than 7 charecters ** "
        return render(request,'list/login.html',dict)
    elif(name == ''):
        dict['signupmessage'] = "Enter a valid name"
        return render(request,'list/login.html',dict)
    elif(adm_no == '' ):
        dict['signupmessage'] = "Enter a valid admission number"
        return render(request,'list/login.html',dict)
    elif(val==1):
        dict['signupmessage']="enter a valid course/class"
    '''try:
        phone = int(phone)
    except Exception, e:
        dict['signupmessage'] = "Enter a valid phone number"
        return render(request,'list/login.html',dict)'''
    data = User.objects.all()
    email_check = User.objects.all().filter(adm_no = adm_no)
    for y in email_check :
        dict['signupmessage'] = "This adm_no is already in use . Please try again with another adm_no "
        return render(request,'list/login.html',dict)
    request.session['logid'] = adm_no


    p = User(name = name,password=password,adm_no=adm_no,phone_no =phone,cbid=i)
    p.save()
    return render(request, 'list/login.html' , {'loginmessage' : " Signup Completed Please check Email and Login to continue "})
