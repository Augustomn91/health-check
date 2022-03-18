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
