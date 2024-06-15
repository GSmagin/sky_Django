from django.urls import path
from catalog.views import home, contacts, product
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product'),

]