from ..models import Appointment

class AppointmentRepository:
    @staticmethod
    def get_all_appointments():
        return Appointment.objects.all()

    @staticmethod
    def get_appointment_by_id(appointment_id):
        return Appointment.objects.get(id=appointment_id)

    @staticmethod
    def create_appointment(appointment_type, duration, availability, admin):
        return Appointment.objects.create(
            appointment_type=appointment_type,
            duration=duration,
            availability=availability,
            admin=admin
        )
