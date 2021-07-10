from django import template

register = template.Library()

@register.filter(name='lookup')
def lookup(dictionary, key):
    return dictionary.get(key)