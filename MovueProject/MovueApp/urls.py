from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('gtyy', views.movie_list,name='movie_list'),
    path('mov/<int:id>/information/', views.information, name="information"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)