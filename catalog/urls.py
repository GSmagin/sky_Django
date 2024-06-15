from django.urls import path
from catalog.views import home_content, contacts, product
from django.conf.urls.static import static

urlpatterns = [
    path('', home_content, name='home_content'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product'),

]