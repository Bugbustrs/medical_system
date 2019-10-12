from django.db import models
from patient.models import Patient

# Create your models here.
class Doctor(models.Model):
    #doctor personal data
    licence_number  = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    
    location = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 14,blank=False, null=False)
    email_address = models.CharField(max_length=100)
    
    medical_scheme = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
  
class Appointment(models.Model):
    
    time = models.DateTimeField()
    
    doctor  = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    