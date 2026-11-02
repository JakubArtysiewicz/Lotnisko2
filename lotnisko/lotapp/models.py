from django.db import models

class Samolot(models.Model):
    typ = models.CharField(max_length=100)
    linie = models.CharField(max_length=100)

class Przyloty(models.Model):
    nr_rejsu = models.IntegerField
    kierunek = models.CharField(max_length=100)
    czas = models.TimeField
    dzien = models.DateField
    statusLotu = models.CharField(max_length=100)
    id_samolotu = models.ForeignKey(Samolot, on_delete=models.CASCADE)

class Odloty(models.Model):
    nr_rejsu = models.IntegerField
    kierunek = models.CharField(max_length=100)
    czas = models.TimeField
    dzien = models.DateField
    statusLotu = models.CharField(max_length=100)
    id_samolotu = models.ForeignKey(Samolot, on_delete=models.CASCADE)

