from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Question(models.Model):
	text      = models.CharField(max_length=200)
	pub_date  = models.DateTimeField('date published')

	def was_published_recently(self):
	    return self.pub_date >= \
	        timezone.now() - datetime.timedelta(days=1)
	
	def __str__(self):
		return "%d: %s" % (self.id, self.text)

class Choice(models.Model):
	question   = models.ForeignKey(Question,
						on_delete=models.CASCADE)
	text       = models.CharField(max_length=200)
	vote_tally = models.IntegerField(default=0)

	def __str__(self):
		return "%s (%d)" % (self.text, self.vote_tally)
