from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/my_work_tpl.html')
def get_photos():
    photos = WorkPhotos.objects.all()
    return {"photos": photos}


