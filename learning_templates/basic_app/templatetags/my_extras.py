from django import template

register = template.Library()


@register.filter(name='cut_arg')
def cut_arg(value,arg):
    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg,'')


#register.filter('cut_arg',cut_arg)