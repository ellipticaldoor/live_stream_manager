from django.views.generic import ListView

from panel.models import Video


class VideoListView(ListView):
	template_name = 'tablet/base_tablet.html'
	model = Video
