from django.urls import path
from .views import ProductList,ProductDetail , BrandDetail, BrandList

app_name = 'Products'
urlpatterns = [
    path('',ProductList.as_view(),name='product_list'),
    path('<slug:slug>',ProductDetail.as_view(),name='product_detail'),


     path('brand',BrandList.as_view(),name='brand_list'),
    path('brand/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),
]