from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # url(r'users/', views.UserDetail.as_view()),
    url(r'posts/', views.QBPostList.as_view()),
    url(r'post/create.json', views.AddPost.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

