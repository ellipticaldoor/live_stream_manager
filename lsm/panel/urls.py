from django.conf.urls import patterns, url

from panel import views


urlpatterns = patterns(
	'',
	url(r'^panel/', views.TimerView.as_view(), name='panel'),
)
