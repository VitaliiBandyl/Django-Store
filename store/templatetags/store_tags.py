from django import template
from store.models import Category, Brand

register = template.Library()

@register.simple_tag()
def get_categories():
    """Displays all categories"""
    return Category.objects.all()


@register.simple_tag()
def get_brands():
    """Displays all brands"""
    return Brand.objects.all()