
from django.urls import path
from photography.views import Photo, Menu

app_name = 'photography'

urlpatterns = [
    path('photo/', Photo, name='Photo'),
    path('', Menu, name='index')

]