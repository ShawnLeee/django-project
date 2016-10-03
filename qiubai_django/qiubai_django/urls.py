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
from django.conf.urls import url, include, patterns
from django.contrib.auth.models import User, Group
from django.contrib import admin

from rest_framework import permissions, routers, selializers, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1.0/', include('api_v_1_0.urls')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
