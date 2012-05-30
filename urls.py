# This also imports the include function
from django.conf.urls.defaults import *
from comments import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'comment_form/', 'mysite.comments.views.comment_form'),
    url(r'^admin/', include(admin.site.urls)),
)