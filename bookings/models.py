from django.db import models


class Patient(models.Model):
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    geburtsdatum = models.DateField()
    telefon = models.CharField(max_length=30)

    def __str__(self):
        return self.vorname + " " + self.nachname


class Termin(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    datum = models.DateField()
    uhrzeit = models.TimeField()
    notiz = models.TextField(blank=True)

    def __str__(self):
        return str(self.datum) + " - " + str(self.patient)