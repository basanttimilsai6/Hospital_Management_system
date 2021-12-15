from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    mobile = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

class Suggest(models.Model):
    email = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.email