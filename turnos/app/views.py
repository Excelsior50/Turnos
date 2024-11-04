from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .controllers.appointment_controller import AppointmentController

class AppointmentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return AppointmentController.list_appointments(request)

    def post(self, request):
        return AppointmentController.create_appointment(request)
