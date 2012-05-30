# -*- coding: UTF-8 -*-
from django import forms
from django.forms import ModelForm

class CommentForm(forms.Form):
	author = forms.CharField(initial='Имя')
	content = forms.CharField(widget=forms.Textarea)
