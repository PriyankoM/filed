# filed
(use post man for send the request)
##Create API
link-http://127.0.0.1:8000/createapi/
method="POST"

###if create "song" object then raw json format-

{"audioFileType":"song",
"audioFileMetadata":{
    "name":"name of the song",
    "duration":time duration in second(only integer)
}
}

###if create "podcast" object then raw json format-

{"audioFileType":"podcast",
"audioFileMetadata":{
    "name":"name of the podcast",
    "duration":time duration in second(only integer),
    "host":"host of your podcast"
}
}

###if create "Audiobook" object then raw json format-

{"audioFileType":"audiobook",
"audioFileMetadata":{
    "title":"title of your audiobook",
    "duration":20000,
    "author":"author name",
    "narrator":"narrator name"
}
}


##Get API
to get all the object

* link- <http://127.0.0.1:8000/getapi/<audioFileType>/<audioFileID>>
    
* example-http://127.0.0.1:8000/getapi/song/2

* http://127.0.0.1:8000/getapi/<audioFileType>  will return all the audio files of that type
    
* example-http://127.0.0.1:8000/getapi/song


##Delete API

http://127.0.0.1:8000/deleteapi/<audioFileType>/<audioFileID>
    
example-  if i want to delete audiobook and it id is 1 then url is- http://127.0.0.1:8000/deleteapi/audiobook/1

##Update API
url- http://127.0.0.1:8000/updateapi/<audioFileType>/<audioFileID>
    
method-"GET"

#if you want to update any "song" then json format will be-
{
    "name":" updated name of the song",
    "duration":time duration of the song (Integer)
}
and url will be-
http://127.0.0.1:8000/updateapi/song/<audioFileID>

#if you want to update any "podcast" then json format will be-
{
    "name":" updated name of the podcast",
    "duration":time duration of the podcast (Integer),
    "host":"host of the podcast"
}
and url will be-
http://127.0.0.1:8000/updateapi/podcast/<audioFileID>

#if you want to update any "audiobook" then json format will be-
{
    "title":" updated name of the s",
    "duration":time duration of the song (Integer),
    "author":"author of this audiobook",
    "narrator":"narrator of this audiobook"
}
and url will be-
http://127.0.0.1:8000/updateapi/audiobook/<audioFileID> 








