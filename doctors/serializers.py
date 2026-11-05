from rest_framework import serializers
from .models import Doctor
from accounts.serializers import UserSerializer
from departments.serializers import DepartmentSerializer

class DoctorSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    department_details = DepartmentSerializer(source='department', read_only=True)

    class Meta:
        model = Doctor
        fields = ('id', 'user', 'user_details',
         'department', 'department_details', 'specialization', 
         'qualification', 'experience_years', 'consultation_fee',
          'bio', 'created_at')