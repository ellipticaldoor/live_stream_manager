from django.conf.urls import patterns, url

from tablet import views


urlpatterns = patterns(
	'',
	url(r'^tablet/$', views.VideoListView.as_view(), name='videos'),
)
