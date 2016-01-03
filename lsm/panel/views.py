from django.views.generic import View, DetailView, ListView

from panel.models import Video


class TimerView(ListView):
	template_name = 'panel/base_panel.html'
	queryset = Video.objects.all()
