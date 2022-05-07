from django.contrib import admin
from django.urls import path
from filmapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', Hello.as_view()),
    path('actors/', ActorAPIView.as_view()),
    path('actors/<int:pk>/', ActorAPIView.as_view()),
]