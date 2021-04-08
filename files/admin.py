from django.contrib import admin
from .models import Song,Podcast,Audiobook


# myModels = [models.Song, models.Podcast, models.Audiobook]  # iterable list
admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(Audiobook)
