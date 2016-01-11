from django.utils import timezone

from django.views.generic import View, DetailView, ListView

from panel.models import Video


class TimerView(ListView):
	template_name = 'timer/base_timer.html'
	queryset = Video

	def get_context_data(self, **kwargs):
		context = super(TimerView, self).get_context_data(**kwargs)
		context['object_list'] = Video.objects.filter(aired_date__gt=timezone.now())
		return context
