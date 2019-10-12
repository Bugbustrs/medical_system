from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    
    email_address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)
    
    blood_type = models.CharField(max_length= 2)
    
class PatientRecord(models.Model):
    #symptonms, diagnosis, prescription
    symptoms = models.CharField(max_length = 1000)
    diagosis  = models.CharField(max_length = 1000)
    prescription = models.CharField(max_length = 1000)
    