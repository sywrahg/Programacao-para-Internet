from django.db import models
# Create your models here.

class User(models.Model):
	#atributos
	email = models.CharField(max_length=45) 
	password = models.CharField(max_length=20)
	birthday = models.DateField(default=None)


	#metodos