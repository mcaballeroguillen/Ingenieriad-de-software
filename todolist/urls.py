from django.conf.urls import url, include
from django.contrib import admin
from . import  views

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^borrar/(?P<activa>[^/]+)$',views.eliminar_actividad, name='eliminar_actividad'),
    url(r'^subir/(?P<activa>[^/]+)$',views.subir_actividad, name='subir_actividad'),
    url(r'^bajar/(?P<activa>[^/]+)$',views.bajar_actividad, name='bajar_actividad'),
]