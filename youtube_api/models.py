from django.db import models



class Latest_results(models.Model):
    video_title=models.CharField(max_length=100)         #Column for the Title of the video
    description=models.CharField(max_length=100)         #Column for the description of the Video
    channel_Title=models.CharField(max_length=100)       #Column for the title of the channel
    date_published=models.DateTimeField(max_length=100)  #Column for the date at which the Video was published

def __str__(self):
    return self.video_title                              #returns the title of the video
