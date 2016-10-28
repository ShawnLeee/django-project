from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # url(r'users/', views.UserDetail.as_view()),
    url(r'posts/$', views.QBPostList.as_view()),
    url(r'post/create.json$', views.AddPost.as_view()),
    url(r'secret$', views.secret_page, name='secret'),
    url(r'post/destory$', views.DeletePost.as_view()),
    url(r'post/show$', views.PostShow.as_view()),
    url(r'comments/show.json$', views.CommentsShow.as_view()),
    url(r'posts/user$', views.PostsUser.as_view()),
    url(r'upload/$', views.Upload.as_view()),
    url(r'comments/by_me.json$', views.UserComments.as_view()),
    url(r'login/$', views.LoginView.as_view()),
    url(r'logout/$', views.LogoutView.as_view()),
    # url(r'^auth-token/', obtain_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)

