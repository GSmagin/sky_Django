from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from catalog.models import Product
from .forms import ProductForm


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
#     return render(request, 'catalog/product.html', context)


class ProductDetailView(DetailView):  # Переопределяем DetailView
    model = Product
    template_name = 'catalog/product.html'


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
    form_class = ProductForm
    success_url = '/catalog/product_form.html'
    # fields = ['name', 'description', 'price', 'category', 'image']  # Поля для создания продукта
    # success_url = reverse_lazy('catalog:product_form')# Перенаправление на список пр


class ProductUpdateView(UpdateView):   # Переопределяем UpdateView для обновления продукта
    model = Product
    form_class = ProductForm
    success_url = '/catalog/product_form.html'
    # fields = ['name', 'description', 'price', 'category', 'image']  # Поля для создания продукта
    # success_url = reverse_lazy('catalog:product_form')# Перенаправление на список пр


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефон: {phone}, Сообщение: {message}')

    return render(request, 'catalog/contacts.html', {'contacts': contacts})
