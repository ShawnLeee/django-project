from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'movies/', views.movies, name='movies'),
    url(r'register/',views.register, name='register'),
]