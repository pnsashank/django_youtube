from django.urls import path,include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'latest_results',views.Latest_resultsViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))   #url for the viewing of the serialized data.
]
