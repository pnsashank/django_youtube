from django.shortcuts import render
from .models import Latest_results
from .serializers import Latest_results_Serializer
from rest_framework import viewsets

class Latest_resultsViewSet(viewsets.ModelViewSet):
    queryset=Latest_results.objects.all().order_by('-date_published')    #view the serialized data in the descending order(in the order of the latest video  
    serializer_class=Latest_results_Serializer
