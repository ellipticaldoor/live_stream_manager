from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from panel import views


urlpatterns = patterns(
	'',
	url(r'^panel/$', login_required(views.TimerView.as_view()), name='panel'),
	url(r'^(?P<pk>[-\w]+)/edit/$', login_required(views.EditTimerView.as_view()), name='edit'),
	url(r'^(?P<pk>[-\w]+)/delete/$', login_required(views.DeleteTimerView.as_view()), name='delete'),
)
