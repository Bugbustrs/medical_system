from django.shortcuts import render
from .models import Patient, PatientRecord
from django.views import generic

# Create your views here.
def index(request):
    return render(request,'patient/index.html',{})

class PatientRecordListView(generic.ListView):
    model = PatientRecord

class PatientRecordDetailView(generic.DetailView):
    model = PatientRecord