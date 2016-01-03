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

	# def get_context_data(self, **kwargs):
	# 	context = super(PostCommitView, self).get_context_data(**kwargs)
	# 	pk, slug = self.kwargs['pk'], self.kwargs['slug']
	# 	context['object'] = Post.objects.by_post(pk, slug)
	# 	return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()

		return super(TimerView, self).form_valid(form)
