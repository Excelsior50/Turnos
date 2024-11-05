from rest_framework import viewsets
from .permissions import IsAdminUser, IsClientUser
from .models import CustomUser, Appointment, Booking
from .serializers import CustomUserSerializer, AppointmentSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .controllers.appointment_controller import AppointmentController

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsClientUser]

