from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path("",views.index,name='home'),
#path("index/",views.signupme,name='singnup'),
path("about/",views.about,name='about'),
path("guide/",views.guide,name='guide'),
path("destination/",views.destination,name='destination'),
path("contact/",views.contact,name='contact'),
]