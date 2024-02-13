from catalog.models import Category
from django.core.cache import cache
from django.conf import settings


def get_cache_category():
    if settings.CACHE_ENABLE:
        key = f'category_list'
        category_list = cache.get(key)
        print('Список категорий')
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
            print('Загружены данные в кеш')
    else:
        category_list = Category.objects.all()

    return category_list
