from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    re_path(r'^api/blog/$', views.lista_blog),
    re_path(r'^api/blog/([0-9])$', views.detalha_blog)
]
