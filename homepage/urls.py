from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('regulamento/', views.regulamento, name="regulamento"),
    path('inscricao/', views.inscricao, name="regulamento"),
    path('evento/<int:id>/', views.ver_evento, name="evento"),
    path('eventos/', views.eventos, name="eventos"),
    path('contato', views.contato, name="contato"),
    path('mensagens/343536/', views.mensagens, name="mensagens"),
    path('mensagem/<int:id>/', views.lido_mensagens, name="mensagem"),
    path('login/', views.loginmsg, name="loginmsg"),
    path('acesso_mensagem/', views.acesso_mensagem, name="acesso_mensagem"),





]
