from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()

        category_list = [
            {'name': 'Алкоголь', 'description': 'Спиртные напитки'},
            {'name': 'Овощи и фрукты', 'description': 'Свежие овощи и фрукты'},
            {'name': 'Хозтовары', 'description': 'Товары для дома, уборки и гигиены'}
        ]

        categories_for_create = []

        for category_item in category_list:
            categories_for_create.append(Category(**category_item))

        Category.objects.bulk_create(categories_for_create)
