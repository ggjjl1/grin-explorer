from django.urls import path

from . import views

app_name = 'blockviewer'
urlpatterns = [
    path('', views.index, name='index'),
]
