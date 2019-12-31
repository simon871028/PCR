from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:character_id>/', views.detail, name='detail'),
    path('create',views.create_data,name='create')
]