from django import template
from blog.models import CategoryPhoto


register = template.Library()


@register.inclusion_tag('blog/category_list_tpl.html')
def show_menu(category_list_class='category_list'):
    categories = CategoryPhoto.objects.all()
    return {"categories": categories, "category_list_class": category_list_class}