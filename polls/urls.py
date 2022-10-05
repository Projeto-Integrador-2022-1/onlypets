from django.urls import path
from polls.views import Splash

urlpatterns = [
    path('', Splash, name='index'),
]
