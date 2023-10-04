from django.contrib import admin
from django.urls import path
from products import urls
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include(urls, namespace='products')),
]
