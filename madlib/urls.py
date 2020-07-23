from django.urls import path
from madlib import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.madlib)
]
urlpatterns += staticfiles_urlpatterns()