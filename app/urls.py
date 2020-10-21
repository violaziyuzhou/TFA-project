from django.urls import path
from . import views
urlpatterns=[
        path('map/',views.map),
        path('sightings/',views.sightings),
        path('sightings/<unique_squirrel_id>',views.unique_squirrel_id),
        path('sightings/add/',views.add) ,
        path('sightings/stats/',views.stats) ,
             ]

