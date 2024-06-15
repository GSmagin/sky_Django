from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from catalog.models import Product
from .forms import ProductForm

# Create your views here.


def home_content(request):
    product = Product.objects.all()
    context = {"product": product}
    return render(request, 'catalog/home_content.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефон: {phone}, Сообщение: {message}')

    return render(request, 'catalog/contacts.html', {'contacts': contacts})


# def product(request, pk):
#     product_list = get_object_or_404(Product, pk=pk)
#     context = {"products": product_list}
#     return render(request, 'catalog/product.html', context)


def product_list(request):
    product = Product.objects.all().order_by('created_at')  # Упорядочиваем по полю created_at
    paginator = Paginator(product, 9)  # 9 продуктов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/product_list.html', {'page_obj': page_obj})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product.html', context)


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})

