from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product
from .forms import ProductForm
from django.db import models


# def product_list(request):
#     product = Product.objects.all().order_by('created_at')  # Упорядочиваем по полю created_at
#     paginator = Paginator(product, 9)  # 9 продуктов на странице
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'catalog/product_list.html', {'page_obj': page_obj})
#

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'catalog/product_detail.html', context)


class ProductDetailView(DetailView):  # Переопределяем DetailView
    model = Product
    template_name = 'catalog/product_detail.html'


# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'catalog/product_form.html', {'form': form})
#


class ProductCreateView(CreateView):  # Переопределяем CreateView для создания продукта
    model = Product
    template_name = 'catalog/product_create.html'
    # template_name = 'catalog/product_form.html'
    fields = ['name', 'description', 'price', 'category', 'image']
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):  # Переопределяем UpdateView для обновления продукта
    model = Product
    template_name = 'catalog/product_update.html'
    # template_name = 'catalog/product_form.html'
    fields = ['name', 'description', 'price', 'category', 'image']
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product  # Переопределяем DeleteView для удаления продукта
    fields = ['name', 'description', 'price', 'category', 'image']
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('product_list')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефон: {phone}, Сообщение: {message}')

    return render(request, 'catalog/contacts.html', {'contacts': contacts})
