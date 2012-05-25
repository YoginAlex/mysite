# -*- coding: UTF-8 -*-
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from comments.models import User, Comment