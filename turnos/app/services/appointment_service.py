from ..repositories.appointment_repository import AppointmentRepository

class AppointmentService:
    @staticmethod
    def list_appointments():
        return AppointmentRepository.get_all_appointments()

    @staticmethod
    def create_appointment(appointment_type, duration, availability, admin):
        return AppointmentRepository.create_appointment(appointment_type, duration, availability, admin)
