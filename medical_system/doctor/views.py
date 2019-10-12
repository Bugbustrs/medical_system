from django.shortcuts import render
from .models import Appointment
from patient.models import PatientRecord
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import PatientRecordForm
from django.forms import modelform_factory
# Create your views here.
class AppointmentListView(generic.ListView):
    model = Appointment

class AppointmentDetailView(generic.DetailView):
    model = Appointment


class PatientRecordCreate(CreateView):
    model = PatientRecord
    def get_form_class(self):
          return modelform_factory(self.model, form=PatientRecordForm, fields=self.fields)

    template_name ='doctor/patientrecord_form.html'
    success_url = '/'