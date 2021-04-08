from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import pytz
from django.core.exceptions import ValidationError




# def validate_date(upload_time):
# 	if upload_time < timezone.now().date():
# 		raise ValidationError("Date cannot be in the past")


def validate_date(upload_time):
	past = datetime.now() - timedelta(days=1)
	# print(past.tzinfo, upload_time.tzinfo,"1st")
	# print(past, upload_time,"2nd")
	if upload_time <= past.replace(tzinfo=pytz.utc):
		# print("@@@@@@@@@@@@@@@@@@@@@@@@")
		raise ValidationError("Date cannot be in the past")	

class Song(models.Model):
	song_title = models.CharField(max_length = 100)
	song_duration = models.PositiveIntegerField()
	upload_time = models.DateTimeField(validators=[validate_date])
	def __str__(self):
		return self.song_title

class Podcast(models.Model):
	podcast_title = models.CharField(max_length = 100)
	podcast_duration = models.PositiveIntegerField()
	upload_time = models.DateTimeField(validators=[validate_date])
	podcast_host = models.CharField(max_length = 100)
	# participants = models.ManyToManyField(User)  

	def __str__(self):
		return self.podcast_title


class Audiobook(models.Model):
	audiobook_title = models.CharField(max_length = 100)
	audiobook_author = models.CharField(max_length = 100)
	audiobook_narrator = models.CharField(max_length = 100)
	audiobook_duration = models.PositiveIntegerField()
	upload_time = models.DateTimeField(validators=[validate_date])

	def __str__(self):
		return self.audiobook_title

