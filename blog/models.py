from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey("auth.User")
	title = models.CharField(max_length = 200)
	content = models.TextField(max_length = 1000)
	date_created = models.DateTimeField(default = timezone.now)
	date_updated = models.DateTimeField(auto_now = True)
	date_published = models.DateTimeField(auto_now = True)
	published = models.BooleanField(default=False)

	def publish(self):
		self.published = True
		self.date_published = timezone.now()
		# must save it so that it saves into the database
		# otherwise it would change in the class instance only
		self.save()

	def __unicode__(self):
		return self.title
