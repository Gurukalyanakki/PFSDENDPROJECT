from django.urls import path
from . import views
from .views import assignment_view

app_name = 'trainerapp'


urlpatterns = [
    path('trainer-home/', views.trainerhomepagecall, name='trainerhomepage'),
    path('courses/', views.course, name='courses'),
    path('ittools/', views.it, name='ittools'),
     path('ittoolls/', views.it2, name='ittools2'),
      path('assignment/', views.assignment_view, name='assignment'),
   
     
]

