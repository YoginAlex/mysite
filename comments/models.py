from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response


# Create your models here.
	
class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    # author = models.ForeignKey(User)
    author = models.TextField()
    page_path = models.TextField()
    def __unicode__(self):
        return self.content
	
	class Meta:
		ordering = ["pub_date"]
