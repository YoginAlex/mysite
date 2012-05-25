from django.db import models
import datetime

# Create your models here.
	
class User(models.Model):
	email = models.EmailField()
	login = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	def __unicode__(self):
		return self.content

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    # parent = models.ForeignKey('self', blank=True, null=True, related_name='child_set')
    author = models.ForeignKey('User')
    def __unicode__(self):
        return self.content
	
	class Meta:
		ordering = ["pub_date"]