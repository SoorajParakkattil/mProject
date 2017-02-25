from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse



class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.course_name

class Batch(models.Model):
    cbname = models.CharField(max_length=15)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    cbid = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.cbname


    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.adm_no})
class User(models.Model):
    name = models.CharField(max_length=20)
    adm_no = models.IntegerField(primary_key=True)
    phone_no = models.IntegerField()
    cbid = models.ForeignKey(Batch, on_delete=models.CASCADE)
    password = models.CharField(max_length = 100)
    isadmin = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Product(models.Model):
    pname = models.CharField(max_length=30)
    product_id = models.AutoField(primary_key=True)
    p_short = models.CharField(max_length=10)
    price = models.FloatField()
    quantity = models.IntegerField()
    product_type = models.CharField(max_length=20)
    brand_name = models.CharField(max_length=20)
    expiry = models.IntegerField()
    expiry_month=models.DateField()
    effective_price = models.FloatField()
    mrp = models.FloatField()
    vat = models.FloatField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.product_id})

    def __str__(self):
        return self.pname
class Purchase(models.Model):
    purch_id = models.AutoField(primary_key=True)
    adm_no = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date=models.DateField()
    remarks = models.CharField(max_length=200)
    response = models.CharField(max_length=200)
    responded = models.IntegerField(default=0)
    placed= models.IntegerField(default=0)

    total = models.FloatField()
    def __str__(self):
        return str(self.purch_id)
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.purch_id})

class Plist(models.Model):
    purch_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    tfield = models.AutoField(primary_key=True)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.tfield)







class Bill(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    bill_date = models.DateTimeField('date of purchase')
    bill_time = models.DateTimeField('time of purchase')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    adm_no = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.adm_no
