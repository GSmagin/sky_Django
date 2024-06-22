from django.urls import path
from .views import (contacts, ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView,
                    ProductDeleteView)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
