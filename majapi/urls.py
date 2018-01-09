"""majapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls.static import static

from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.conf import settings

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'products', views.ProductList, base_name='products')
router.register(r'wishlist', views.WishListList, base_name='wishlist')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.LoginList.as_view()),
    # url(r'^products/', views.ProductList.as_view()),
    # url(r'^wishList/', views.WishListList.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^', include(router.urls, namespace='catalog')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)
