from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=200)
    creacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Curso(models.Model):
    nombre= models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add = True)
    Estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return '%s' % (self.nombre)

class Telefono(models.Model):
    tipo_telefono = (
        ('C', 'Casa'),
        ('M', 'Movil'),
        ('T','Trabajo'),
    )
    telefono= models.CharField(max_length=13)
    estudiante = models.ForeignKey(Estudiante,on_delete = models.CASCADE)
    tipo = models.CharField(
        max_length= 1,
        choices = tipo_telefono,
        default = 'C',
    )
    creacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % (self.telefono)

class EstudianteAut(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=200)
    creacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Articulo(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.descripcion)

class Comentario(models.Model):
    comentario = models.CharField(max_length=100)
    Estudiante = models.ManyToManyField(Estudiante)
    Articulo = models.ManyToManyField(Articulo)
    creacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % (self.comentario)

class Administrador(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=200)
    creacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)
