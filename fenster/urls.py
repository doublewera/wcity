from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', views.buy, name='buy'),
    path('add/', views.add, name='add'),
    # по 'name' можно вызвать функцию в шаблоне по тэгу {% url %} 
]
