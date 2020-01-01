from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_data, name='create'),
    path('list/', views.character_list, name='character_list')
]
