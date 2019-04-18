from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='buy'),
    #path('<int:fenster_id>/', views.buy, name='buy'),
    # по 'name' можно вызвать функцию в шаблоне по тэгу {% url %} 
]
