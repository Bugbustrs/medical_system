from django.contrib import admin
from django.urls import path
from .views import AppointmentDetailView,AppointmentListView

urlpatterns = [
   
    path('appointments',AppointmentListView.as_view(),name='appointment_list'),
    path('appointments/<int:pk>',AppointmentDetailView.as_view(),name='appointment_detail'),

]