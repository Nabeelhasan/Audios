from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import SongSerializer,AudiobookSerializer,PodcastSerializer
from .models import Song,Audiobook,Podcast
from rest_framework import status
from django.http import HttpResponse
from datetime import datetime
import ast
from rest_framework.decorators import parser_classes
import json
from django.shortcuts import get_object_or_404


@api_view(["GET"])
@csrf_exempt
def get_file(request,audioFileType,pk):
	if audioFileType == 'Song':
		song = Song.objects.get(id = pk)
		serializer = SongSerializer(song)
		return JsonResponse(serializer.data,safe=False)
	if audioFileType == 'Podcast':
		podcast = Podcast.objects.get(id = pk)
		serializer = PodcastSerializer(podcast)
		return JsonResponse(serializer.data,safe=False)
	if audioFileType == 'Audiobook':
		audiobook = Audiobook.objects.get(id = pk)
		serializer = AudiobookSerializer(audiobook)
		return JsonResponse(serializer.data,safe=False)

@api_view(["GET"])
@csrf_exempt
def get_allfile(request,audioFileType):
	if audioFileType == 'Song':
		song = Song.objects.all()
		serializer = SongSerializer(song,many=True)
		# print(serializer.data)
		return JsonResponse(serializer.data,safe=False)
	if audioFileType == 'Podcast':
		podcast = Podcast.objects.all()
		serializer = PodcastSerializer(podcast,many=True)
		return JsonResponse(serializer.data,safe=False)
	if audioFileType == 'Audiobook':
		audiobook = Audiobook.objects.all()
		serializer = AudiobookSerializer(audiobook,many=True)
		return JsonResponse(serializer.data,safe=False)
	


@api_view(["PUT"])
@csrf_exempt
def update_file(request,audioFileType,pk):
	# meta_Data = request.POST.get('audioFileMetaData',False)
	meta_data = json.loads(request.data['audioFileMetaData'])
	print(meta_data)
	try:
		if audioFileType == 'Song':
			# print("7777777777777777777777777777777777777777777")
			# song = Song.objects.get(id = pk)
			song = get_object_or_404(Song, pk=pk)
			print(song.song_duration)
			serializer = SongSerializer(song, data={'song_title':meta_data.get('song_title'),
													'song_duration':meta_data.get('song_duration'),
													'upload_time':datetime.strptime(meta_data.get('upload_time'),"%Y-%m-%d")}, partial=True)
				
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
				
			else:
				return Response("An error occured",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

		if audioFileType == 'Podcast':
			podcast = get_object_or_404(Podcast, pk=pk)
			# print(meta_data)
			serializer = PodcastSerializer(podcast,data = {'podcast_title':meta_data.get('podcast_title'),
												'podcast_duration':meta_data.get('podcast_duration'),
												'upload_time':datetime.strptime(meta_data.get('upload_time'),"%Y-%m-%d"),
												'podcast_host':meta_data.get('podcast_host')
												},partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
				
			else:
				return Response("An error occured",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
			
		if audioFileType == 'Audiobook':
			audiobook = get_object_or_404(Audiobook,pk=pk)
			serializer = AudiobookSerializer(audiobook,data = {'audiobook_title':meta_data.get('audiobook_title'),
												'audiobook_author':meta_data.get('audiobook_author'),
												'upload_time':datetime.strptime(meta_data.get('upload_time'),"%Y-%m-%d"),
												'audiobook_narrator':meta_data.get('audiobook_narrator'),
												'audiobook_duration':meta_data.get('audiobook_duration')
												},partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
				
			else:
				return Response("An error occured",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	except Exception as e:
		# print(e)
		return Response("The request is invalid",status = status.HTTP_400_BAD_REQUEST)



@api_view(["DELETE"])
@csrf_exempt
def delete_file(request,audioFileType,pk):
	if audioFileType == 'Song':
		song = Song.objects.get(id = pk)
		song.delete()

	if audioFileType == 'Podcast':
		podcast = Podcast.objects.get(id = pk)
		podcast.delete()

	if audioFileType == 'Audiobook':
		audiobook = Audiobook.objects.get(id = pk)
		audiobook.delete()
		
	return Response("Action is successful",status=status.HTTP_200_OK)




@api_view(["POST"])
@csrf_exempt
def create_file(request):
	# print(request.POST)
	file_type = request.POST.get('audioFileType',False)
	# meta_Data = request.POST.get('audioFileMetaData',False)
	# print(file_type)
	# print(request.data)
	meta_data = json.loads(request.data['audioFileMetaData'])
	
	if file_type and meta_data:
		try:
			if file_type == 'Song':
				serializer = SongSerializer(data = {'song_title':meta_data.get('song_title'),
													'song_duration':meta_data.get('song_duration'),
													'upload_time':datetime.strptime(meta_data.get('upload_time'),"%Y-%m-%d")})
				
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data, status=status.HTTP_200_OK)
					
				else:
					return Response("An error occured",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

			if file_type == 'Podcast':
				serializer = PodcastSerializer(data = {'podcast_title':meta_data.get('podcast_title'),
													'podcast_duration':meta_data.get('podcast_duration'),
													'upload_time':datetime.strptime(meta_data.get('upload_time'),"%Y-%m-%d"),
													'podcast_host':meta_data.get('podcast_host')
													})
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data, status=status.HTTP_200_OK)
					
				else:
					return Response("An error occured",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
			
			if file_type == 'Audiobook':
				serializer = AudiobookSerializer(data = {'audiobook_title':meta_data.get('audiobook_title'),
													'audiobook_author':meta_data.get('audiobook_author'),
													'upload_time':datetime.strptime(meta_data.get('upload_time'),"%Y-%m-%d"),
													'audiobook_narrator':meta_data.get('audiobook_narrator'),
													'audiobook_duration':meta_data.get('audiobook_duration')
													})
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data, status=status.HTTP_200_OK)
					
				else:
					return Response("An error occured",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		except Exception as e:
			return Response("The request is invalid",status = status.HTTP_400_BAD_REQUEST)