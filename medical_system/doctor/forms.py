from django import forms
from patient.models import PatientRecord


class PatientRecordForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields =['symptoms','diagnosis','prescription']
        widgets ={
            'symptoms':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter symptoms here'}),
            'diagnosis':forms.Textarea(attrs={'class':'form-control','placeholder':'Describe diagnosis'}),
            'prescription':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter prescription'}),

 
            }