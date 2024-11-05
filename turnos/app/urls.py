from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, AppointmentViewSet, BookingViewSet
from .controllers.appointment_controller import AppointmentController

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
