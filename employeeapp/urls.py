from django.urls import path,include
from . import views

app_name='employeeapp'
urlpatterns=[
    path('employeehomepage',views.employeehomepagecall,name='employeehomepage')
]