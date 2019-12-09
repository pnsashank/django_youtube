from background_task import background
import requests
from .models import Latest_results
from django.conf import settings
@background(schedule=10)       #the task of quering the data from the youtube api is scheduled every 10 seconds
def api_call():
    search_url = 'https://www.googleapis.com/youtube/v3/search'      #the youtbe api endpoint for making search requests
    search_params={
        'part':'snippet',
        'q':'cricket',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'order':'date',
        'type':'video'
        }                                                            #the search parameters with query as 'cricket'
    r=requests.get(search_url,params=search_params)
    results=r.json()['items']                                        #json format of the request output of the jey 'items'
    for i in range(0,len(results)):
        result="result"+'_'+str(i)                                   #parameter name to the Latest_results class (ORM)
        videoTitle=results[i]['snippet']['title']                    #the title of video
        Description=results[i]['snippet']['description']             #the description of the video
        datePublished=results[i]['snippet']['publishedAt']           #Date at which the video is published
        channelTitle=results[i]['snippet']['channelTitle']            #the Id of the channel
        result=Latest_results(video_title=videoTitle,description=Description,channel_Title=channelTitle,date_published=datePublished) #Pushing the data to the Latest_results database through ORM
        result.save()   #saving the data to the colums if Latest_results of the database
api_call(repeat=10) #repeat after 10 seconds
