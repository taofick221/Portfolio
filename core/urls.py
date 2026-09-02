from django.urls import path
from .views import home, resume

urlpatterns = [
    path("", home, name="home"),
    path("resume/", resume, name="resume"),
]
