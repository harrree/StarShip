from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list,name='movie_list'),
    path('mov/<int:id>',views.information,name="information"),
]
