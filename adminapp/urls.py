from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.homepagecall,name='projecthomepage'),
    path('loginpagecall/', views.loginpagecall, name='loginpagecall'),
    path('registerpagecall/', views.registerpagecall, name='registerpagecall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
  
]