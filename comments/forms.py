# -*- coding: UTF-8 -*-
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.db import models
from comments.models import *

class CommentForm(ModelForm):
	author = forms.CharField()
	class Meta:
		model = Comment
		fields = ('author', 'content',)
	# author = forms.CharField(initial='Имя')
	# content = forms.CharField(widget=forms.Textarea)
