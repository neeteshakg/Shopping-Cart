# templatetags/tag_library.py

from django import template

register = template.Library()

@register.filter()
def to_int(value,data):
    return int(value*data)


def sum(value):
    varsum = varsum + value
    return varsum
