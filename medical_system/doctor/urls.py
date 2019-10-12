from django.contrib import admin
from django.urls import path
from .views import AppointmentDetailView,AppointmentListView, PatientRecordCreate

urlpatterns = [
   
    path('appointments',AppointmentListView.as_view(),name='appointment_list'),
    path('appointments/<int:pk>',AppointmentDetailView.as_view(),name='appointment_detail'),
    path('create-record/',PatientRecordCreate.as_view(),name='create_patient_record'),

]