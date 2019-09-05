from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Permission, User


class User(AbstractUser):

    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Enviroment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.CharField(max_length=200, default= '', verbose_name='Descrição', blank=True)

    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'


class Board(models.Model):
    name = models.CharField(max_length=30, verbose_name='Placa')
    description = models.CharField(max_length=250, default= '', verbose_name='Descrição', blank=True)

    class Meta:
        verbose_name = 'Placa'
        verbose_name_plural = 'Placas'


class Type(models.Model):
    typeDate = models.CharField(max_length=10, verbose_name='Tipo')
    unity = models.CharField(max_length=10, verbose_name='Unidade')

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class Sensor(models.Model):
    description = models.CharField(max_length=255, default= '', verbose_name='Descrição', blank=True)
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    type_sensor = models.ForeignKey(Type, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'


class Data(models.Model):
    value = models.CharField(max_length=100,verbose_name='Valor')
    date = models.DateField(max_length=100, verbose_name='Data')
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, blank=True)

    class Meta:
        verbose_name = 'Dado do Sensor'
        verbose_name_plural = 'Dados do Sensor'
