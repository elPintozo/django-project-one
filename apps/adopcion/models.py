from django.db import models

# Create your models here.
class Persona(models.Model):
	##id_manual = models.CharField(max_length=10,primary_key=True) <- sólo si quiero asignar de forma manual el id
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=50)
	email = models.EmailField()
	direccion = models.TextField()

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)

class Solicitud(models.Model):
	persona = models.ForeignKey(Persona, null=True, blank=True)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()