from django.urls import path
from pet.views import PetCad,ListaPet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ListaPet,name='listapet'),
    path('petcad/', PetCad,name='petcad'),
]