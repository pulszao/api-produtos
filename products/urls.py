# -*- encoding:utf-8 -*-
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from .views import Products, ProductData

app_name = "products"

urlpatterns = [
    path("", Products.as_view(), name="products"),
    path("<int:product_id>", ProductData.as_view(), name="product_data"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
