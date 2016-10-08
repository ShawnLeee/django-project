"""qiubai_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#from rest_framework import permissions, routers, selializers, viewsets

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1.0/', include('api_v_1_0.urls')),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^accounts/login/$', include('django.contrib.auth.views.login')),
    # url(r'^accounts/logout/$', include('django.contrib.views.logout')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
