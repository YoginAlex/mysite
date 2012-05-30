# -*- coding: UTF-8 -*-
from django import template
from django.db import models
from django.contrib.auth.models import User
import datetime
from mysite.comments.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

register = template.Library()

@register.inclusion_tag('comments/tags/comments.html')
def commentslist(request):
	form = CommentForm()
	return {"form": form, "request": request}
