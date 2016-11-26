# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter(name='bt_to')
def bt_to(value):
    if "b" in value:
        return value.replace("b", "回表")
    elif "t" in value:
        return value.replace("t", "回裏")