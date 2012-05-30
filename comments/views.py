# -*- coding: UTF-8 -*-
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from comments.models import *
from comments.forms import CommentForm
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.template.loader import render_to_string
# Я пока плохо понял - какие модули следует импортировать, а какие нет... Где всё это почитать?

def comment_form(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid()
			pass
	return HttpResponseRedirect(request.META['HTTP_REFERER'])
