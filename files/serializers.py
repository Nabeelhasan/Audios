from rest_framework import serializers
from .models import Song,Audiobook,Podcast

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = '__all__'
		# fields = ['song_title','song_duration','upload_time']
		# partial = True

class PodcastSerializer(serializers.ModelSerializer):
	class Meta:
		model = Podcast
		fields = '__all__'


class AudiobookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Audiobook
		fields = '__all__'

