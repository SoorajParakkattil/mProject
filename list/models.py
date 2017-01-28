from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Product(models.Model):
    pname = models.CharField(max_length=30)
    product_id = models.CharField(max_length=20, primary_key=True)
    price = models.FloatField()
    quantity = models.FloatField()
    product_type = models.CharField(max_length=20)
    brand_name = models.CharField(max_length=20)
    expiry = models.FloatField()
    effective_price = models.FloatField()
    mrp = models.FloatField()
    vat = models.FloatField()

    def get_absolute_url(self):
        return reverse('list/detail.html',kwargs={'pk':self.product_id})

    def __str__(self):
        return self.pname


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


class User(models.Model):
    name = models.CharField(max_length=20)
    adm_no = models.IntegerField(primary_key=True)
    phone_no = models.IntegerField()
    cbid = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Bill(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    bill_date = models.DateTimeField('date of purchase')
    bill_time = models.DateTimeField('time of purchase')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    adm_no = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.adm_no
