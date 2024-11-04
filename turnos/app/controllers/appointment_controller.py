from rest_framework.response import Response
from rest_framework import status
from ..services.appointment_service import AppointmentService
from ..serializers import AppointmentSerializer

class AppointmentController:
    @staticmethod
    def list_appointments(request):
        appointments = AppointmentService.list_appointments()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    @staticmethod
    def create_appointment(request):
        data = request.data
        appointment = AppointmentService.create_appointment(
            appointment_type=data['appointment_type'],
            duration=data['duration'],
            availability=data['availability'],
            admin=request.user
        )
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
