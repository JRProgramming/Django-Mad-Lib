from django.urls import path
from tutorial import views

urlpatterns = [
    path("", views.home, name="home"),
]