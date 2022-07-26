from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    id_proyecto = models.CharField(max_length = 10, null = False)
    nombre = models.CharField(max_length=100, null=False)
    cliente = models.CharField(max_length=100, null=True, blank=True)
    trello = models.URLField(null=True)
    fecha_inicio = models.DateField(null = False)
    fecha_entrega = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=10, null = True, blank=True)


class Cliente(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    nombre = models.CharField(max_length=100, null=False)
    contacto = models.CharField(max_length=100, null=False)


class Costo(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    detalle = models.CharField(max_length=100, null=True, blank=True)
    monto_un = models.FloatField(null=False)
    un = models.IntegerField(null=False)
    total = models.FloatField(null=False)   
    id_proyecto = models.ForeignKey(Project, on_delete=models.CASCADE)

class Ingreso(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    fecha = models.DateField(null = False)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    detalle = models.CharField(max_length=100, null=True, blank=True)
    total = models.FloatField(null=False)
    id_proyecto = models.ForeignKey(Project, on_delete=models.CASCADE)


class Gasto(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    fecha = models.DateField(null=False)
    lugar = models.CharField(max_length=100, null=True, blank=True)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    detalle = models.CharField(max_length=100, null=True, blank=True)
    monto_un = models.FloatField(null=False)
    un = models.IntegerField(null=False)
    total = models.FloatField(null=False)
