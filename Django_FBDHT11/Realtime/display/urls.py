from django.contrib import admin
from django.urls import path

from display import views

urlpatterns = [
    path("",views.index, name='display'),
    path("about",views.about, name='about'),
    path("team",views.team, name='team'),
    path("datalist",views.datalist, name='datalist')
]
