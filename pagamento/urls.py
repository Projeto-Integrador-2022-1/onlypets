from django.urls import path
from login.views import HomeLogin,Logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeLogin,name='login'),
    path('logout/', Logout,name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)