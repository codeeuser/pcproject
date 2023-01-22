from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('system_info', views.system_info, name='system_info'),
    path('system_info_json', views.system_info_json, name='system_info_json'),
]