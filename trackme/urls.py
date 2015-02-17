from django.conf.urls import patterns, url
from trackme import views

urlpatterns = patterns('',
	url(r'^$',views.index,name = 'index'),
	url(r'^login/$',views.login,name='login'),
	url(r'^register/$',views.register,name='register'),
	url(r'^(?P<username>\w+)/profile/$',views.profile,name = 'profile'),
	
)