from trackme.models import *
# Create your views here.
from django.views import generic
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, render_to_response, redirect

class IndexView(generic.ListView):
	template_name = 'trackme/index.html'
	context_object_name = 'users'
	def get_queryset(self):
		return User.objects.order_by('username')


def register(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        profilePicture = request.POST['profilePicture']
        newUser = User.objects.create(username = username, password = password, email = email, reports = 0 , profilePicture = profilePicture)
        if newUser is not None :
            return HttpResponseRedirect(reverse('trackme/profile.html'))
    return render_to_response('trackme/register.html', context_instance=RequestContext(request))


def login(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('trackme/profile.html',context_instance = RequestContext(request))
    return render_to_response('trackme/login.html', context_instance=RequestContext(request))


class ProfileView(generic.DetailView):
    template_name = 'trackme/profile.html'
    context_object_name = 'users'
    def get_queryset(self):
        return User.objects.filter(username='username')

