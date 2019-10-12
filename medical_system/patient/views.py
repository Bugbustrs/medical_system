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

class PatientRecordCreationView(CreateView):
    model = PatientRecord
    fields=('symptoms','diagnosis','prescription')