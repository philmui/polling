from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Question(models.Model):
	text      = models.CharField(max_length=200)
	pub_date  = models.DateTimeField('date published')

	def was_published_recently(self):
	    now = timezone.now()
	    return now >= self.pub_date >= \
	        now - datetime.timedelta(days=1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	
	def __str__(self):
		return "%s" % (self.text,)

class Choice(models.Model):
	question   = models.ForeignKey(Question,
						on_delete=models.CASCADE)
	text       = models.CharField(max_length=200)
	vote_tally = models.IntegerField(default=0)

	def __str__(self):
		return "%s" % (self.text,)
