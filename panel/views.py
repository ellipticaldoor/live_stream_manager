from datetime import datetime

from django.views.generic.edit import CreateView, UpdateView

from panel.models import Video
from panel.forms import TimerForm


class TimerView(CreateView):
	template_name = 'panel/base_panel.html'
	form_class = TimerForm
	success_url = '/panel/'

	def get_context_data(self, **kwargs):
		context = super(TimerView, self).get_context_data(**kwargs)
		context['videos'] = Video.objects.filter(aired_date__gte=datetime.now())
		context['next_video_date'] = context['videos'][0]
		context['my_videos'] = Video.objects.filter(user=str(self.request.user))
		context['all_videos'] = Video.objects.all()
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.aired_date = '%s %s' % (self.request._post["date"], self.request._post["time"])
		obj.save()
		return super(TimerView, self).form_valid(form)


class EditTimerView(UpdateView):
	template_name = 'panel/base_panel.html'
	form_class = TimerForm
	success_url = '/panel/'
	model = Video

	def get_context_data(self, **kwargs):
		context = super(EditTimerView, self).get_context_data(**kwargs)
		context['edit_video'] = Video.objects.filter(pk=self.kwargs['pk'])[0]
		context['videos'] = Video.objects.filter(aired_date__gte=datetime.now())
		context['next_video_date'] = context['videos'][0]
		print(Video.objects.filter(pk=self.kwargs['pk']))
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.aired_date = '%s %s' % (self.request._post["date"], self.request._post["time"])
		obj.save()
		return super(EditTimerView, self).form_valid(form)
