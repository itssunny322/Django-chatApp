from django.contrib import admin
from django.urls import path

from .views import home, login_web, room, personal, register, getchat

urlpatterns = [
    path('home/',home,name='home'),
    path('login/',login_web,name='login_web'),
    path('register/',register,name='register'),
    path('room/<str:room_name>/', room, name='room'),
    path('personal/<str:user_id>/', personal, name='personal'),
    path('chat/history/', getchat, name='getchat'),

]
