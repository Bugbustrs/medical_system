from django.db import models
from django.urls import reverse 

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    
    email_address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)
    
    blood_type = models.CharField(max_length= 2)
    
class PatientRecord(models.Model):
    #symptonms, diagnosis, prescription
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,blank=True, null=True)
    symptoms = models.TextField(max_length = 1000)
    diagosis  = models.TextField(max_length = 1000)
    prescription = models.TextField(max_length = 1000)
    date = models.DateField(auto_now_add=True, blank=True,null=True)
    
    def get_absolute_url(self):
        return reverse("patientrecord_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.diagosis
    