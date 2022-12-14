"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from only.views import Homep,Clinica,Vet
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('', Splash, name='splash'),
    path('', Homep,name='home'),
    path("login/", include("login.urls")),
    path("cadastro/",include("cadastro.urls")),
    path("clinica/",Clinica,name='clinica'),
    path("admin/", admin.site.urls),
    path("vet/<id>/",Vet,name='vet'),
    path("pet/",include("pet.urls")),
    path("vetpage/",include("veterinario.urls")),
    path("carrinho/",include("cart.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
