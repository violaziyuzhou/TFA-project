from django.urls import path
from . import views
urlpatterns=[path("",views.map),
             path("",views.get_post_request),
             path("",views.get_request) ,

             ]

