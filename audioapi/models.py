from django.db import models
from django.utils.timezone import now

# Create your models here.

class Song(models.Model):
    song_id=models.AutoField
    song_name=models.CharField(max_length=100,null=False)
    song_duration=models.IntegerField(null=False)
    song_uploaded_time=models.DateTimeField(default=now)

class Podcast(models.Model):
    podcast_id=models.AutoField
    podcast_name=models.CharField(max_length=100,null=False)
    podcast_duration=models.IntegerField(null=False)
    podcast_uploaded_time=models.DateTimeField(default=now)
    podcast_host=models.CharField(max_length=100,null=False)

class Audiobook(models.Model):
    audiobook_id=models.AutoField
    audiobook_title=models.CharField(max_length=100,null=False)
    audiobook_author=models.CharField(max_length=100,null=False)
    audiobook_narrator=models.CharField(max_length=100,null=False)
    audiobook_duration=models.IntegerField(null=False)
    audiobook_uploaded_time=models.DateTimeField(default=now)


    
