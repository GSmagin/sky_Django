from django.urls import path
from catalog.views import home, contacts

urlpatterns = [
    path('home/', home, name='catalog/home'),
    path('contacts/', contacts, name='catalog/contacts'),

]
