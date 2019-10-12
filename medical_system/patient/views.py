from django.shortcuts import render
from .models import Patient, PatientRecord
from doctor.models import Appointment
from django.views import generic
from django.views.generic.edit import CreateView
# Create your views here.
def index(request):
    return render(request,'patient/index.html',{})

class PatientRecordListView(generic.ListView):
    model = PatientRecord

class PatientRecordDetailView(generic.DetailView):
    model = PatientRecord

class AppointmentListView(generic.ListView):
    model = Appointment

class AppointmentDetailView(generic.DetailView):
    model = Appointment
