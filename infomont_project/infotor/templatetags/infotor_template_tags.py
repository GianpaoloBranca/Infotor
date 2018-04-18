from django import template

register = template.Library()

@register.simple_tag
def verbose_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name

@register.simple_tag
def max_length(obj, field_name):
    return obj._meta.get_field(field_name).max_length

@register.inclusion_tag('infotor/torrent_edit_field.html')
def render_edit_field(obj, field_name, field_value=None):

    field = obj._meta.get_field(field_name)

    field_type = field.get_internal_type()
    field_choices = field.choices
    field_max_length = field.max_length

    return {'type': field_type,
            'max_length': field_max_length,
            'choices': field_choices,
            'value': field_value}


#@register.simple_tag
#def choices(obj, field_name):
#    return obj._meta.get_field(field_name).choices

#@register.simple_tag
#def field_type(obj, field_name):
#    return obj._meta.get_field(field_name).get_internal_type()
