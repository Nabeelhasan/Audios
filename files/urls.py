from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('create/',views.create_file,name='create_file'),
	path('delete/<str:audioFileType>/<int:pk>/',views.delete_file,name='delete_file'),
	path('get/<str:audioFileType>/<int:pk>/',views.get_file,name='get_file'),
	path('get/<str:audioFileType>/',views.get_allfile,name='get_allfile'),
	path('update/<str:audioFileType>/<int:pk>/',views.update_file,name='update_file')

	# path('createTest/',views.song_list,name='song_list')
    # path('',include('files.urls'))
]