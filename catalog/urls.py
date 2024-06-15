from django.urls import path
from catalog.views import home, contacts, products
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', products, name='products'),

]