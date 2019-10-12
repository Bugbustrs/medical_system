from django.contrib import admin
from django.urls import path
from .views import index, PatientRecordListView,PatientRecordDetailView

urlpatterns = [
    path('',index,name='index'),
    path('records/',PatientRecordListView.as_view(),name='patientrecord-list'),
    path('records/<int:pk>',PatientRecordDetailView.as_view(),name='patientrecord_detail'),

]