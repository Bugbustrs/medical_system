from django.shortcuts import render
from .models import Appointment
from django.views import generic

# Create your views here.
class AppointmentListView(generic.ListView):
    model = Appointment

class AppointmentDetailView(generic.DetailView):
    model = Appointment


