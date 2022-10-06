from django.urls import path
from polls.views import Splash,Homep,Login,Cadastro

urlpatterns = [
    path('', Splash, name='splash'),
    path("home/", Homep,name='home'),
    path("login/", Login,name='login'),
    path("cadastro/",Cadastro,name='cadastro'),
]
