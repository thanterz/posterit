from rest_framework import serializers
from django.forms import widgets
from models import poster_type,payment_method,addresses,orders,order_products
from models import materials,categories,photos
from django.contrib.auth.models import User


class paymentMethodSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = payment_method

class posterTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = poster_type

class addressesSerializer(serializers.ModelSerializer):
	class Meta:
		model = addresses

class ordersSerializer(serializers.ModelSerializer):
	class Meta:
		model = orders

class orderProductsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = order_products

class materialsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = materials

class categoriesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = categories

class photosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = photos