from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.movie_list,name='movie_list'),
    path('search/', views.search,name='search'),
    path('mov/<int:id>/information/', views.information, name="information"),
    path('mov/<int:id>/review/', views.review, name="review"),
    re_path(r'^mov/(?P<id>\d*)?/edit/$', views.edit, name="edit"),
    re_path(r'^mov/(?P<id>\d*)?/dele/$', views.dele, name="dele"),
    path('watchlist/', views.watchlist, name="watchlist"),
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('login/', views.userlogin, name="userlogin"),
    path('register/', views.register, name="register"),
    path('logout/', views.userlogout, name="userlogout"),
    path('reaction/<int:rid>/', views.reaction, name='reaction'),

    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
         name="password_reset"),

    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
         name="password_reset_confirm"),

    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="password_done.html"), 
         name="password_reset_complete"),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   