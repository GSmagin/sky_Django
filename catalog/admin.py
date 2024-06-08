from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
