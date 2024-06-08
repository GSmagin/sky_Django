import json
import os
import django
from django.core.management.base import BaseCommand
from catalog.models import Product, Category


def setup_django():
    # Установите переменную окружения DJANGO_SETTINGS_MODULE
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    # Загрузите настройки Django
    django.setup()


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    @staticmethod
    def json_read(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_categories():
        return Command.json_read('catalog/fixtures/categories.json')

    @staticmethod
    def json_read_products():
        return Command.json_read('catalog/fixtures/products.json')

    def handle(self, *args, **options):
        # Удалить все продукты
        Product.objects.all().delete()
        # Удалить все категории
        Category.objects.all().delete()

        # Создать списки для хранения объектов
        category_for_create = []
        product_for_create = []

        # Обойти все значения категорий из фикстуры для получения информации об одном объекте
        for category_data in self.json_read_categories():
            fields = category_data['fields']
            category_for_create.append(
                Category(
                    id=category_data['pk'],
                    name=fields['name'],
                    description=fields.get('description', '')
                )
            )

        # Создать объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обойти все значения продуктов из фикстуры для получения информации об одном объекте
        for product_data in self.json_read_products():
            fields = product_data['fields']
            product_for_create.append(
                Product(
                    id=product_data['pk'],
                    name=fields['name'],
                    description=fields.get('description', ''),
                    image=fields.get('image', ''),
                    category=Category.objects.get(pk=fields['category']),
                    price=fields['price'],
                    created_at=fields['created_at'],
                    updated_at=fields['updated_at']
                )
            )

        # Создать объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

        self.stdout.write(self.style.SUCCESS('Database has been populated successfully.'))


