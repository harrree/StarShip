from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.movie_list,name='movie_list'),
    path('search/', views.search,name='search'),
    path('mov/<int:id>/information/', views.information, name="information"),
    path('mov/<int:id>/review/', views.review, name="review"),
    re_path(r'^mov/(?P<id>\d*)?/edit/$', views.edit, name="edit"),
    re_path(r'^mov/(?P<id>\d*)?/dele/$', views.dele, name="dele"),
    path('watchlist/', views.watchlist, name="watchlist"),
    path('profile/', views.profile, name="profile"),
    path('vwatchlist/', views.vwatchlist, name="vwatchlist"),
    path('login/', views.userlogin, name="userlogin"),
    path('register/', views.register, name="register"),
    path('logout/', views.userlogout, name="userlogout")
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   