import subprocess


def dump_data(file_path, apps):
    try:
        command = [
            'python', '-Xutf8', 'manage.py', 'dumpdata', apps, '--indent', '4'
        ]

        command_to_file = f"{' '.join(command)} > {file_path}"

        subprocess.run(command_to_file, shell=True, check=True)
        print(f"Data dump completed successfully. File saved as {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


catalog_category = 'catalog.Category'
catalog_product = 'catalog.Product'

dump_data("catalog/fixtures/categories.json", catalog_category)
dump_data("catalog/fixtures/products.json", catalog_product)

#python -Xutf8 manage.py dumpdata catalog.Category catalog.Product --indent 4 > catalog/fixtures/initial_data.json