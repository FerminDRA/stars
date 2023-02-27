from django.db import models

# Create your models here.
class Estrella(models.Model):
    nombre=models.TextField(default='', blank=False)
    distancia=models.TextField(default='', blank=False)
    radio=models.FloatField(default=0, blank=False)
    rotacion=models.FloatField(default=0, blank=False)
    edad=models.IntegerField(default=0, blank=False)
    ubicacion=models.IntegerField(default=0, blank=False)
    masa=models.IntegerField(default=0, blank=False)
    temperatura=models.FloatField(default=0, blank=False)
    constelacion=models.TextField(default='', blank=False)
    color=models.TextField(default='', blank=False)
