from rest_framework import serializers
from .models import Latest_results

class Latest_results_Serializer(serializers.HyperlinkedModelSerializer):    #For the serilization of the data in the databse to json
    class Meta:
        model=Latest_results
        fields=('video_title','description','channel_Title','date_published')
