from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers, serializers, viewsets

from panel import views

from panel.models import Video
from user.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username',)

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Video
		fields = ('videoid', 'user', 'videourlid', 'aired_date')


class VideoViewSet(viewsets.ModelViewSet):
	queryset = Video.objects.all()
	serializer_class = VideoSerializer


router = routers.DefaultRouter()
router.register(r'video', VideoViewSet)

urlpatterns = patterns(
	'',
	url(r'^rest/', include(router.urls)),
	url(r'^panel/$', login_required(views.TimerView.as_view()), name='panel'),
	url(r'^(?P<pk>[-\w]+)/edit/$', login_required(views.EditTimerView.as_view()), name='edit'),
	url(r'^(?P<pk>[-\w]+)/delete/$', login_required(views.DeleteTimerView.as_view()), name='delete'),
)
