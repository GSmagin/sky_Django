import json
import os
import django
from django.apps import apps
from django.conf import settings
from catalog.models import Category, Product

# Установка Django окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


DATA_FILE = './catalog/fixtures/initial_data.json'


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def clear_data():
    Category.objects.all().delete()
    Product.objects.all().delete()


def populate_data(data):
    for item in data:
        model = apps.get_model(item['model'])
        pk = item['pk']
        fields = item['fields']
        obj, created = model.objects.update_or_create(pk=pk, defaults=fields)
        if created:
            print(f'Created: {model.__name__} {obj.pk}')
        else:
            print(f'Updated: {model.__name__} {obj.pk}')


def main():
    data = load_data(DATA_FILE)
    clear_data()
    populate_data(data)
    print("Database has been populated successfully.")


if __name__ == '__main__':
    main()
