from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import StaffCreateSerializer

from .serializers import (
    UserRegisterSerializer,
    UserSerializer
)

User = get_user_model()


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user



class StaffCreateView(generics.CreateAPIView):
    serializer_class = StaffCreateSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return User.objects.none()



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]