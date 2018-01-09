# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Login, Products, WishList
from .serializers import LoginSerialzer, ProductSerialzer, WishListSerialzer


# Create your views here.

#login/
class LoginList(APIView):

    def get(self, request):
        login = Login.objects.all()
        serializer = LoginSerialzer(login, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LoginSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#products/
class ProductList(viewsets.ModelViewSet):
    serializer_class = ProductSerialzer

    def get_queryset(self):
        return Products.objects.all()

#wishList/

class WishListList(viewsets.ModelViewSet):
    serializer_class = WishListSerialzer

    def get_queryset(self):
        userId = self.request.query_params.get("user")
        if userId:
            return WishList.objects.filter(user=userId)
        return WishList.objects.all()
