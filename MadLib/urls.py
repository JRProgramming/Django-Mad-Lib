from django.urls import path
from MadLib import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.madlib)
]
urlpatterns += staticfiles_urlpatterns()