from django.contrib import admin
from .models import Estudiante,Curso,Telefono,EstudianteAut,Articulo,Comentario

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Telefono)
admin.site.register(EstudianteAut)
admin.site.register(Articulo)
admin.site.register(Comentario)