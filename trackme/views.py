from trackme.models import *
# Create your views here.
from django.views import generic
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, render_to_response, redirect


def index(request):
    return render_to_response('trackme/index.html',{'users':User.objects.order_by('username')})


def register(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        profilePicture = request.POST['profilePicture']
        newUser = User.objects.create(username = username, password = password, email = email, reports = 0 , profilePicture = profilePicture)
        if newUser is not None :
            return HttpResponseRedirect(reverse('trackme:profile', args = (username,)))
    return render_to_response('trackme/register.html', context_instance=RequestContext(request))


def login(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username = username, password = password)
        if len(user) > 0:
            return HttpResponseRedirect(reverse('trackme:profile', args = (username,)))
    return render_to_response('trackme/login.html', context_instance=RequestContext(request))


def profile(request,username):
    if username is not None:
        return render_to_response('trackme/profile.html',{'user':User.objects.filter(username = username)[1]})
    return render_to_response('trackme/login.html')

