from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import EstudianteForm, EstudianteAutForm, ArticuloForm, ComentarioForm, AdministradorForm
from django.urls import reverse_lazy 

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class AdministradoresView(TemplateView):
    template_name='administradores.html'

class EstudiantesView(TemplateView):
    template_name='estudiantes.html'

class CrearEstudiantesView(CreateView):
    template_name='crearestudiantes.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('home:homeapp')

class CrearEstudianteAutsView(CreateView):
    template_name='crearestudianteauts.html'
    form_class = EstudianteAutForm
    success_url = reverse_lazy('home:homeapp')

class CrearArticulosView(CreateView):
    template_name='creararticulos.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('home:homeapp')

class CrearComentariosView(CreateView):
    template_name='crearcomentarios.html'
    form_class = ComentarioForm
    success_url = reverse_lazy('home:homeapp')

class CrearAdministradoresView(CreateView):
    template_name='crearadministradores.html'
    form_class = AdministradorForm
    success_url = reverse_lazy('home:homeapp')

class IniciosesionView(TemplateView):
    template_name='iniciosesion.html'
    