from django.urls import path

from . import views

#route to 
urlpatterns = [
   # method inside the views file 
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]