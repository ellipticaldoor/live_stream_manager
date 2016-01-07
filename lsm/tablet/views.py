from datetime import datetime
from django.views.generic import ListView

from panel.models import Video


class VideoListView(ListView):
	template_name = 'tablet/base_tablet.html'
	model = Video

	def get_context_data(self, **kwargs):
		context = super(VideoListView, self).get_context_data(**kwargs)
		context['object_list'] = Video.objects.filter(aired_date__lt=datetime.now())
		return context
