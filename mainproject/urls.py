"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'api/payment_methdod',views.paymentMethodViewSet)
router.register(r'api/poster_type',views.posterTypeViewSet)
router.register(r'api/addresses',views.addressesViewSet)
router.register(r'api/orders',views.ordersViewSet)
router.register(r'api/user/(?P<uid>\d+)/orders',views.userordersViewSet,base_name="orders")
router.register(r'api/products',views.orderProductsViewSet)
router.register(r'api/materials',views.materialsViewSet)
router.register(r'api/user/(?P<uid>\d+)/addresses',views.useraddressesViewSet,base_name="addresses")


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)), 
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]
