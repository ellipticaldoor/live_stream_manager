from django.views.generic.edit import CreateView
from django.views.generic import View, DetailView, ListView

from panel.models import Video
from panel.forms import TimerForm


# class TimerView(ListView):
# 	template_name = 'panel/base_panel.html'
# 	queryset = Video.objects.all()

class TimerView(CreateView):
	template_name = 'panel/base_panel.html'
	form_class = TimerForm
	success_url = '/panel/'

	def get_context_data(self, **kwargs):
		context = super(TimerView, self).get_context_data(**kwargs)
		context['videos'] = Video.objects.all()
		return context

	def form_valid(self, form):

		print(self.request._post["date"])
		print(self.request._post["time"])

		obj = form.save(commit=False)
		obj.user = self.request.user
		# obj.aired_date = "2016-01-03 21:37:06.097035+00";
		obj.aired_date = '%s %s' % (self.request._post["date"], self.request._post["time"])
		obj.save()

		return super(TimerView, self).form_valid(form)
