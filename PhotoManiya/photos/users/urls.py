from django.urls import path
from users.views import login, profile, registration, new_photo

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('registration/', registration, name='registration'),
    path('new_photo/', new_photo, name='new_photo')

]