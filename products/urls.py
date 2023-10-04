# -*- encoding:utf-8 -*-
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from .views import Products

app_name = "products"

urlpatterns = [
    path("", Products.as_view(), name="products"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
