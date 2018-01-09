# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Login, Products, WishList

# Register your models here.

admin.site.register(Login)
admin.site.register(Products)
admin.site.register(WishList)


