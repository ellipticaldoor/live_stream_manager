from django import forms

from panel.models import Video


class TimerForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = ('videourlid',)
