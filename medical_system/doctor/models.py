from django.db import models
from patient.models import Patient
from django.urls import reverse

# Create your models here.
class Doctor(models.Model):
    #doctor personal data
    licence_number  = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    
    location = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 14,blank=False, null=False)
    email_address = models.CharField(max_length=100)
    
    medical_scheme = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("doctor_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.first_name
    
  
class Appointment(models.Model):
    
    date= models.DateField(null=True)
    time = models.TimeField(null=True)    
    doctor  = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return "appointment with Dr "+self.doctor.first_name+" "+ self.doctor.surname
    
    def get_absolute_url(self):
        return reverse("appointment_detail", kwargs={"pk": self.pk})
    
    