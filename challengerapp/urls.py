from django.contrib import admin
from django.urls import path
from .views import indexfunc,News,Store,Look,Video,About,Stockist


urlpatterns = [
    path('',indexfunc),
    path('news/',News.as_view(),name='news'),
    path('store/',Store.as_view(),name='store'),
    path('look/',Look.as_view(),name='look'),
    path('video/',Video.as_view(),name='video'),
    path('about/',About.as_view(),name='about'),
    path('stockist/',Stockist.as_view(),name='stockist'),
]