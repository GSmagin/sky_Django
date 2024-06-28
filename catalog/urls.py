from django.urls import path

from .apps import CatalogConfig
from .views import (contacts, ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView,
                    ProductDeleteView, BlogPostListView, BlogPostCreateView, BlogPostDetailView, BlogPostUpdateView,
                    BlogPostDeleteView, BlogCreateView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('blog/list/', BlogPostListView.as_view(), name='blogpost_list'),
    path('blog/сreate/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blog/detail/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blog/update/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('blog/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]
