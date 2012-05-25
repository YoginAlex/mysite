# -*- coding: UTF-8 -*-
from django import template
from django.db import models
import datetime

register = template.Library()

@register.inclusion_tag('comments/tags/comments.html')
def commentslist(commentform):
	if commentform:
		value = 'Включено'
	else:
		value = 'Выключено'
	return { 
    'value': value,
    }