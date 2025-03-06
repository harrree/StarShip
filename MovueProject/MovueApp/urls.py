from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.movie_list,name='movie_list'),
    path('search/', views.search,name='search'),
    path('mov/<int:id>/information/', views.information, name="information"),
    path('mov/edit/', views.edit, name="edit"),
    path('watchlist/', views.watchlist, name="watchlist"),
    path('profile/', views.profile, name="profile"),
    path('vwatchlist/', views.vwatchlist, name="vwatchlist"),
    path('login/', views.userlogin, name="userlogin"),
    path('register/', views.register, name="register"),
    path('logout/', views.userlogout, name="userlogout"),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   