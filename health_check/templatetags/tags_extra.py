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
        return 'color: #d61818;'
    elif value == 'back':
        return 'color: #d4a517;'
    elif value == 'homol':
        return 'color: #18d3d6;'
    elif value == 'prod':
        return 'color: #18d63c;'


@register.filter(name='bootstrap_model')
def name_bootstrap_model(value):
    if value == 'front':
        return 'badge rounded-pill bg-dark border border-danger'
    elif value == 'back':
        return 'badge rounded-pill bg-dark border border-warning'
    elif value == 'homol':
        return 'badge rounded-pill bg-dark border border-info'
    elif value == 'prod':
        return 'badge rounded-pill bg-dark border border-success'