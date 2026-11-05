from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        DOCTOR = 'DOCTOR', 'Doctor'
        PATIENT = 'PATIENT', 'Patient'
        RECEPTIONIST = 'RECEPTIONIST', 'Receptionist'

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.PATIENT
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):

        if self.role == self.Role.ADMIN:
            self.is_staff = True

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"