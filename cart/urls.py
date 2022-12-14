from django.urls import path
from cart.views import Carrinho,conf_pag,histo


urlpatterns = [
path('<id>/',Carrinho,name='carrinho'),
path('<id>/pagamento/',conf_pag,name='conf_pag'),
path('<id>/histo',histo,name='histo'),
]