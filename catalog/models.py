from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', )
    date_of_last_mod = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')

    # created_at = models.TextField(max_length=100, verbose_name='Тест с отменой миграции', null=True)

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=50, verbose_name='Слаг')
    content = models.TextField(max_length=500, verbose_name='Содержимое')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication_sign = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
