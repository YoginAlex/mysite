from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import datetime

# Create your models here.
	
class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User)
    page_path = models.TextField()
    def __unicode__(self):
        return self.content
	
	class Meta:
		ordering = ["pub_date"]