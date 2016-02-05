from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import posterTypeSerializer,paymentMethodSerializer,addressesSerializer
from api.serializers import ordersSerializer,materialsSerializer
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

class ordersViewSet(viewsets.ModelViewSet):
	allowed_methods = ('GET','POST', 'PUT', 'DELETE','HEAD','OPTIONS')
	queryset = orders.objects.all()
	serializer_class = ordersSerializer