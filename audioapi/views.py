from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import dateutil.parser
from .models import Song
from .models import Podcast
from .models import Audiobook
# Create your views here.


@csrf_exempt
def createapi(request):
    if request.method=="POST":
        try:
            mydata = json.loads(request.body.decode("utf-8"))
            if mydata["audioFileType"].lower()=="song":
                name=mydata["audioFileMetadata"]["name"]
                duration=mydata["audioFileMetadata"]["duration"]
                song_obj=Song(song_name=name,song_duration=duration)
                song_obj.save()
                return HttpResponse('Action is successful: 200 OK')
            elif mydata["audioFileType"].lower()=="podcast":
                name=mydata["audioFileMetadata"]["name"]
                duration=mydata["audioFileMetadata"]["duration"]
                host=mydata["audioFileMetadata"]["host"]
                podcast_obj=Podcast(podcast_name=name,podcast_duration=duration,podcast_host=host)
                podcast_obj.save()
                return HttpResponse('Action is successful: 200 OK')
            elif mydata["audioFileType"].lower()=="audiobook":
                title=mydata["audioFileMetadata"]["title"]
                author=mydata["audioFileMetadata"]["author"]
                narrator=mydata["audioFileMetadata"]["narrator"]
                duration=mydata["audioFileMetadata"]["duration"]
                audiobook_obj=Audiobook(audiobook_title=title,audiobook_author=author,audiobook_narrator=narrator,audiobook_duration=duration)
                return HttpResponse('Action is successful: 200 OK')
            else:
                return HttpResponse("The request is invalid: 400 bad request")
        except:
            return HttpResponse('500 internal server error')
    else:    
        return HttpResponse("The request is invalid: 400 bad request")

@csrf_exempt
def getapi(request,audioFileType,audioFileID=None):
    try:
        if audioFileType.lower()=="song":
            if audioFileID is not None:
                songdata=Song.objects.filter(id=int(audioFileID))[0]
                dic={"song id":songdata.id,"song name":songdata.song_name,"song duration":songdata.song_duration,"song uploaded time":str(songdata.song_uploaded_time)}
                return JsonResponse(dic)
            else:
                l=[]
                songdata=list(Song.objects.all())
                for i in songdata:
                    l.append({"song id":i.id,"song name":i.song_name,"song duration":i.song_duration,"song uploaded time":str(i.song_uploaded_time)})
                l1=json.dumps(l)  
                return JsonResponse(l1,safe=False)

        elif audioFileType.lower()=="podcast":
            if audioFileID is not None:
                podcastdata=Podcast.objects.filter(id=int(audioFileID))[0]
                dic={"podcast_id":podcastdata.id,"podcast_name":podcastdata.podcast_name,"podcast_duration":podcastdata.podcast_duration,"podcast_uploaded_time":str(podcastdata.podcast_uploaded_time),"host":podcastdata.podcast_host}
                return JsonResponse(dic)
            else:
                l=[]
                podcastdata=list(Podcast.objects.all())
                for i in podcastdata:
                    l.append({"podcast_id":i.id,"podcast_name":i.podcast_name,"podcast_duration":i.podcast_duration,"podcast_uploaded_time":str(i.podcast_uploaded_time),"host":i.podcast_host})
                l1=json.dumps(l)  
                return JsonResponse(l1,safe=False)
        elif audioFileType.lower()=="audiobook":
            if audioFileID is not None:
                audiobookdata=Audiobook.objects.filter(id=int(audioFileID))[0]
                dic={"audiobook_id":audiobookdata.id,"audiobook_title":audiobookdata.audiobook_title,"audiobook_author":audiobookdata.audiobook_author,"audiobook_uploaded_time":str(audiobookdata.audiobook_uploaded_time),"audiobook_narrator":audiobookdata.audiobook_narrator,"audiobook_duration":audiobookdata.audiobook_duration}
                return JsonResponse(dic)
            else:
                l=[]
                audiobookdata=list(Audiobook.objects.all())
                for i in audiobookdata:
                    l.append({"audiobook_id":i.id,"audiobook_title":i.audiobook_title,"audiobook_author":i.audiobook_author,"audiobook_uploaded_time":str(i.audiobook_uploaded_time),"audiobook_narrator":i.audiobook_narrator,"audiobook_duration":i.audiobook_duration})
                l1=json.dumps(l)  
                return JsonResponse(l1,safe=False)
        else:
            return HttpResponse("The request is invalid: 400 bad request")
    except:        
        return HttpResponse('500 internal server error')
    


@csrf_exempt
def deleteapi(request,audioFileType,audioFileID):
    try:
        if audioFileType.lower()=="song":
            del_item=Song.objects.get(id=int(audioFileID))
            del_item.delete()
            return HttpResponse('Action is successful: 200 OK')
        elif audioFileType.lower()=="podcast":
            del_item=Podcast.objects.get(id=int(audioFileID))
            del_item.delete()
            return HttpResponse('Action is successful: 200 OK')
        elif audioFileType.lower()=="audiobook":
            del_item=Audiobook.objects.get(id=int(audioFileID))
            del_item.delete()
            return HttpResponse('Action is successful: 200 OK')  
        else:
            return HttpResponse("The request is invalid: 400 bad request")
    except:
        return HttpResponse("500 internal server error")



@csrf_exempt
def updateapi(request,audioFileType,audioFileID):
    try:
        mydata = json.loads(request.body.decode("utf-8"))
        if audioFileType.lower()=="song":
            update_item=Song.objects.get(id=int(audioFileID))
            update_item.song_name=mydata["name"]
            update_item.song_duration=mydata["duration"]
            update_item.save()
            return HttpResponse('Action is successful: 200 OK')
        elif audioFileType.lower()=="podcast":
            update_item=Podcast.objects.get(id=int(audioFileID))
            update_item.podcast_name=mydata["name"]
            update_item.podcast_duration=mydata["duration"]
            update_item.podcast_host=mydata["host"]
            update_item.save()
            return HttpResponse('Action is successful: 200 OK')
        elif audioFileType.lower()=="audiobook":
            update_item=Audiobook.objects.get(id=int(audioFileID))
            update_item.audiobook_title=mydata["title"]
            update_item.audiobook_author=mydata["author"]
            update_item.audiobook_narrator=mydata["narrator"]
            update_item.audiobook_duration=mydata["duration"]
            return HttpResponse('Action is successful: 200 OK')  
        else:
            return HttpResponse("The request is invalid: 400 bad request")
    except:
        return HttpResponse("500 internal server error")



