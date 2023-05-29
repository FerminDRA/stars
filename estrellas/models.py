from django.db import models
from django.conf import settings

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
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    estrella = models.ForeignKey('estrellas.Estrella', related_name='votes', on_delete=models.CASCADE)
