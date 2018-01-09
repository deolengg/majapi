# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class Login(models.Model):
    emailId = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.emailId



class Products(models.Model):
    pName = models.CharField(max_length=25)
    pImage = models.ImageField(upload_to="static/images/", default="/media")
    pDesc = models.CharField(max_length=100)
    pRating = models.PositiveIntegerField(default=0)
    pPrice = models.PositiveIntegerField(default=0)
    pQty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.pName

class WishList(models.Model):
    user = models.CharField(max_length=128)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
