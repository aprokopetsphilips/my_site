"""
URL configuration for drf_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from women.views import *
from rest_framework import routers

#router = routers.SimpleRouter()
#router.register(r'women', WomenViewSet)  # https://www.django-rest-framework.org/api-guide/routers/    and  https://www.django-rest-framework.org/api-guide/authentication/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')), # https://djoser.readthedocs.io/en/latest/
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenApiUpdate.as_view() ),
    path('api/v1/womendelete/<int:pk>/', WomenApiDetailView.as_view()),
    path('api/v1/auth/', include('djoser.urls')), # эта и следующая строка для подключения djoser
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    #path('api/v1/', include(router.urls)),

]
