from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Transporteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    username = models.CharField(max_length=150, default='') 
    raison_sociale = models.CharField(max_length=100)
    tel_tax = models.CharField(max_length=20)
    email = models.EmailField()
    nif = models.CharField(max_length=20)
    numero_rs = models.CharField(max_length=20)
    numero_bt_camion = models.CharField(max_length=20)

class Chauffeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    username = models.CharField(max_length=150,  default='') 
    numero_pc = models.CharField(max_length=20)
    date_pc = models.DateField()
