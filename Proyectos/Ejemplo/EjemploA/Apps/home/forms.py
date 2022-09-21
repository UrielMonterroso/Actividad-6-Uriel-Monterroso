from django import forms
from .models import Estudiante, EstudianteAut, Articulo, Comentario, Administrador

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class EstudianteAutForm(forms.ModelForm):
    class Meta:
        model = EstudianteAut
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'