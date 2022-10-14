"""EjemploA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from .views import HomeView,AdministradoresView,EstudiantesView,CrearEstudiantesView,CrearEstudianteAutsView,CrearArticulosView,CrearComentariosView,CrearAdministradoresView,IniciosesionView,RegistroView,LoginView
from Apps.home import views

app_name='home'

urlpatterns = [
    path('',HomeView.as_view(), name='homeapp'),
    path('administradores/',AdministradoresView.as_view(), name='administradoresapp'),
    path('estudiantes/',EstudiantesView.as_view(), name='estudiantesapp'),
    path('crearestudiantes/',CrearEstudiantesView.as_view(), name='crearestudiantesapp'),
    path('crearestudianteauts/',CrearEstudianteAutsView.as_view(), name='crearestudianteautsapp'),
    path('creararticulos/',CrearArticulosView.as_view(), name='creararticulosapp'),
    path('crearcomentarios/',CrearComentariosView.as_view(), name='crearcomentariosapp'),
    path('crearadministradores/',CrearAdministradoresView.as_view(), name='crearadministradoresapp'),
    path('iniciosesion/',IniciosesionView.as_view(), name='iniciosesionapp'),
    path('registro/',RegistroView.as_view(), name='registroapp'),
    path('login/',LoginView.as_view(), name='loginapp'),
    
]
