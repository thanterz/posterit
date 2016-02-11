from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import posterTypeSerializer,paymentMethodSerializer,addressesSerializer
from api.serializers import ordersSerializer,materialsSerializer,useraddressesSerializer
from api.serializers import orderProductsSerializer,categoriesSerializer
from models import poster_type,payment_method,addresses,orders,order_products
from models import materials,categories,photos 
from django.core import serializers
from django.core.mail import send_mail
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D
from django.contrib.auth.models import User
from rest_framework import permissions

# Create your views here.

class paymentMethodViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = payment_method.objects.all()
	serializer_class = paymentMethodSerializer

class posterTypeViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = poster_type.objects.all()
	serializer_class = posterTypeSerializer

class addressesViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = addresses.objects.all()
	serializer_class = addressesSerializer

class useraddressesViewSet(viewsets.ViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	def list(self,request,uid=None):
		queryset = addresses.objects.filter(user=uid)
		serializer = useraddressesSerializer(queryset,many=True,context={'request': request})
		return Response(serializer.data)

class ordersViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = orders.objects.all()
	serializer_class = ordersSerializer

class userordersViewSet(viewsets.ViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	def list(self,request,uid=None):
		queryset = orders.objects.filter(client=uid)
		serializer = ordersSerializer(queryset,many=True,context={'request':request})
		return Response(serializer.data)

class orderProductsViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = order_products.objects.all()
	serializer_class = orderProductsSerializer

class materialsViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = materials.objects.all()
	serializer_class = materialsSerializer