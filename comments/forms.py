# -*- coding: UTF-8 -*-
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.db import models
from comments.models import *

class CommentForm(forms.Form):
    # author = models.ForeignKey(User)
    author = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    page_path = forms.CharField(widget=forms.HiddenInput())
