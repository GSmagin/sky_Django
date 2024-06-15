from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.

def home(request):
    product_list = Product.objects.all()
    context = {"product": product_list}
    return render(request,  'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефон: {phone}, Сообщение: {message}')

    return render(request, 'catalog/contacts.html', {'contacts': contacts})


def products(request, pk):
    product_list = get_object_or_404(Product, pk=pk)
    context = {"products": product_list}
    return render(request, 'catalog/products.html', context)

