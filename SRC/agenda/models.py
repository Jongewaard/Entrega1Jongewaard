from django.db import models
import datetime

# Create your models here.
class agenda(models.Model):
    apynombre = models.CharField(max_length=100, default="default")
    f_nac = models.DateField(default=datetime.datetime.now())
    e_mail = models.EmailField(default="example@example.com")

    def __str__(self) -> str:
        return f'{self.apynombre}'

class calendario(models.Model):
    nombre_evento = models.CharField(max_length=100, default="evento")
    f_evento = models.DateTimeField(default=datetime.datetime.now())
    f_aviso_evento = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self) -> str:
        return f'{self.nombre_evento} {self.f_evento}'

class bitacora(models.Model):
    fecha = models.DateField(default=datetime.datetime.now())
    titulo = models.CharField(max_length=20, default="titulo")
    momento = models.TimeField(default=datetime.datetime.now())
    sucesos = models.CharField(max_length=300, default="default")

    def __str__(self) -> str:
        return f'{self.fecha} {self.titulo}'
