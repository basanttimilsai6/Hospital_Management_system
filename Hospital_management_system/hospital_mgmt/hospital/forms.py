from django.forms.models import ALL_FIELDS
from .models import Doctor, Patient, Appointment
from django import forms
from django.db.models import fields

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'