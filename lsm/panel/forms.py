from django import forms

from panel.models import Video


class TimerForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TimerForm, self).__init__(*args, **kwargs)
		self.fields['videourlid'].widget.attrs.update({
				'required': 'required',
			})

	class Meta:
		model = Video
		fields = ('videourlid',)
