from datetime import datetime

from django.views.generic import View, DetailView, ListView

from panel.models import Video


class TimerView(ListView):
	template_name = 'timer/base_timer.html'
	queryset = Video.objects.filter(aired_date__gte=datetime.now())
