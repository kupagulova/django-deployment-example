from django import template

register = template.Library()
@register.filter(name = 'cut_value')
def cut_value(value,arg):
    """
    This cuts out all values of arg from string

    """

    return value.replace(arg,'')

# register.filter('cut_value',cut_value)
