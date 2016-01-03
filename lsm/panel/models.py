from django.db import models

from user.models import User
from core.core import _createId

class Video(models.Model):
	STATUS_CHOICES = (
		('live', 'live'),
		('recorded', 'recorded'),
	)

	videoid = models.CharField(primary_key=True, max_length=16, default=_createId)
	user = models.ForeignKey(User, related_name='videos')
	status = models.CharField(db_index=True, max_length=10, choices=STATUS_CHOICES, default='live')
	created = models.DateTimeField(auto_now_add=True)

	# objects = VideoQuerySet.as_manager()

	def save(self, *args, **kwargs):
		super(Video, self).save(*args, **kwargs)

	def __str__(self):
		return self.videoid

	class Meta:
		verbose_name_plural = 'Videos'
		ordering = ['-created']
