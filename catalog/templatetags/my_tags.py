from django import template
from django.conf import settings

register = template.Library()


# Создание тега
@register.simple_tag
def path_media(image):
    return f'{settings.MEDIA_URL}{image}'
