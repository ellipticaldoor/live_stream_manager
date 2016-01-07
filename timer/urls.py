from django.conf.urls import patterns, url

from timer import views


urlpatterns = patterns(
	'',
	url(r'^$', views.TimerView.as_view(), name='timer'),
)
