import json
import os
import django
from django.core.management.base import BaseCommand
from catalog.models import Product, Category


# def setup_django():
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
#     django.setup()
#

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
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category_data in self.json_read_categories():
            fields = category_data['fields']
            category_for_create.append(
                Category(
                    id=category_data['pk'],
                    name=fields['name'],
                    description=fields.get('description', '')
                )
            )

        Category.objects.bulk_create(category_for_create)

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

        Product.objects.bulk_create(product_for_create)

        self.stdout.write(self.style.SUCCESS('!!! Successfully created initial data!!!'))



# (venv) PS D:\Skypro\sky_Django> python manage.py loaddata .\catalog\fixtures\products.json
# Installed 3 object(s) from 1 fixture(s)
# (venv) PS D:\Skypro\sky_Django>
