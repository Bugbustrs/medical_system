from django.contrib import admin
from .models import Patient, PatientRecord

# Register your models here.
admin.site.register(Patient)
admin.site.register(PatientRecord)
