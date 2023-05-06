from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=100)
	text = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)

	def Publicar(self):
		self.fecha_creacion = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo