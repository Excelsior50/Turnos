from django.urls import path
from app.views import AppointmentListView

urlpatterns = [
    path('appointments/', AppointmentListView.as_view(), name='appointment-list')
]
