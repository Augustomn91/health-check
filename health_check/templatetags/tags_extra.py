from django import template

register = template.Library()


@register.filter(name='badge')
def status_bagde(value):
    if value in range(100, 399):
        return "success"
    elif value < 500:
        return "warning"
    else:
        return "danger"


@register.filter(name='name_tag')
def name_tag_badge(value):
    if value == 'front':
        return 'red'
    elif value == 'back':
        return 'blue'
    elif value == 'homol':
        return 'green'
    elif value == 'prod':
        return 'black'
