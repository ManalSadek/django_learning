from django.conf.urls import patterns, url
from trackme import views

urlpatterns = patterns('',
	url(r'^$',views.IndexView.as_view(),name = 'index'),
	url(r'^login/$',views.login,name='login'),
	url(r'^register/$',views.register,name='register'),
	url(r'^profile/$',views.ProfileView.as_view(),name = 'profile'),
	
)