from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.gis.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class poster_type(models.Model):
	name = models.CharField(max_length=40)
	price = models.FloatField()

class materials(models.Model):
	material_type = models.CharField(max_length=20)
	price = models.IntegerField()

class payment_method(models.Model):
	payment = models.CharField(max_length=20)

class addresses(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	phone = models.IntegerField()
	street = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	county = models.CharField(max_length=20)
	postal_code = models.IntegerField()
	address_name = models.CharField(max_length=50)
	created = DateTimeField(auto_now_add=True, blank=True)

class orders(models.Model):
	STATUS_OPTIONS = (
		('Pending', 'Pending'),
		('Approved', 'Approved'),
		('Denied', 'Denied'),
	) 
	order_status = models.CharField(max_length=10,choices=STATUS_OPTIONS)
	order_total = models.IntegerField()
	paymentm = models.ForeignKey(payment_method,related_name='%(class)s_payment')
	created = models.DateTimeField(auto_now_add=True, blank=True)
	client = models.ForeignKey(User,related_name='%(class)s_user_id')

class order_products(models.Model):
	orderid = models.ForeignKey(orders,related_name='order')
	postertp = models.ForeignKey(poster_type,related_name='type')
	mat = models.ForeignKey(materials,related_name='material')
	billing = models.ForeignKey(addresses,related_name='billing_info')
	delivery = models.ForeignKey(addresses,related_name='delivery_info')

class categories(models.Model):
	category = models.CharField(max_length=20)
	imgcat = models.ImageField(upload_to='category_image',default='')

class user_photos(models.Model):
	image = models.ImageField(upload_to='user',default='')
	uid = models.ForeignKey(User,related_name='user_id')

class photos(models.Model):
	path = models.ImageField(upload_to='photos',default='')
	usid = models.ForeignKey(User,related_name='%(class)s_userid')
	categ = models.ForeignKey(categories,related_name='%(class)s_category')