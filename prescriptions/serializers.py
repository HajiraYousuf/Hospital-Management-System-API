from rest_framework import serializers
from .models import Prescription
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer

class PrescriptionSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)

    class Meta:
        model = Prescription
        fields = ('id', 'patient', 'patient_details', 'doctor', 'doctor_details', 'appointment', 'medicines', 'instructions', 'created_at')