from django import template

register = template.Library()

@register.simple_tag
def verbose_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name

@register.simple_tag
def max_length(obj, field_name):
    return obj._meta.get_field(field_name).max_length
