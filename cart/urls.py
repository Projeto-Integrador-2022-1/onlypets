from django.urls import path,include
from cart.views import Carrinho

urlpatterns = [
path('<id>/',Carrinho,name='carrinho'),
]