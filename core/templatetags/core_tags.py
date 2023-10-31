from django import template

from core.models import Menu

register = template.Library()


@register.inclusion_tag('core/menu.html')
def menu_tag(title, request):
    menu = Menu.objects.filter(title=title).prefetch_related(
        'menu_item__children__children__children'
    ).first()
    current_link = request.path
    return {'menu': menu,
            'current_link': current_link}
