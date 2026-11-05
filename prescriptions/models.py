from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True, related_name='prescriptions')
    medicines = models.TextField(help_text="List of medicines with dosage instructions")
    instructions = models.TextField(blank=True, null=True, help_text="Additional doctor notes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient} by {self.doctor}"