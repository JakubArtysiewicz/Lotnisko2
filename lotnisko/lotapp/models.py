from django.db import models

class Samolot(models.Model):
    typ = models.TextField()
    linie = models.TextField()

class Odloty(models.Model):
    nr_rejsu = models.IntegerField()
    kierunek = models.TextField()