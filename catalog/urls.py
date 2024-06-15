from django.urls import path
from catalog.views import home_content, contacts, product_detail, product_list, product_create
from django.conf.urls.static import static

urlpatterns = [
    path('', product_list, name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/new/', product_create, name='product_create'),
]
