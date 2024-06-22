from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from catalog.models import Product, BlogPost
from .forms import ProductForm
from django.db import models

from .utils.mail_newsletter import congratulate_mail_newsletter


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


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog/blogpost_detail.html'
    context_object_name = 'blogpost'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        congratulate_mail_newsletter(obj)
        return obj


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog/blogpost_list.html'
    context_object_name = 'blogposts'
    paginate_by = 10

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'catalog/blog/blogpost_form.html'
    fields = ["title", "content", "preview_image", "is_published"]
    success_url = reverse_lazy('blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blogpost_detail", args=[self.object.pk])


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ("title", "content", "preview_image", "is_published")
    template_name = 'catalog/blog/blogpost_form.html'
    context_object_name = 'blogpost'
    success_url = reverse_lazy('blogpost_detail')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blogpost_detail", args=[self.object.pk])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')


class BlogCreateView(TemplateView):
    template_name = 'catalog/blog.html'

